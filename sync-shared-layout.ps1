$ErrorActionPreference = "Stop"

# Run from the website root
$rootDir = Split-Path -Parent $MyInvocation.MyCommand.Path
$sourceFile = Join-Path $rootDir "index.html"

if (-not (Test-Path $sourceFile)) {
    throw "Root index.html not found at: $sourceFile"
}

$sourceHtml = Get-Content -Path $sourceFile -Raw -Encoding UTF8

# Extract everything shared before <main id="main-content">
$headerPattern = '(?s)<a class="skip-link" href="#main-content">.*?(?=<main id="main-content">)'
$headerMatch = [regex]::Match($sourceHtml, $headerPattern)

if (-not $headerMatch.Success) {
    throw "Could not extract shared header/nav block from root index.html"
}

$sharedHeader = $headerMatch.Value.TrimEnd()

# Extract shared footer/tail from the homepage
$footerPattern = '(?s)<div class="mountain-divider purple-mountain" aria-hidden="true"></div>.*?</html>\s*'
$footerMatch = [regex]::Match($sourceHtml, $footerPattern)

if (-not $footerMatch.Success) {
    throw "Could not extract shared footer/tail block from root index.html"
}

$sharedFooter = $footerMatch.Value.TrimEnd()

# Extract schema block from homepage head
$schemaPattern = '(?s)<script\s+type="application/ld\+json">\s*.*?\s*</script>'
$schemaMatch = [regex]::Match($sourceHtml, $schemaPattern)

if (-not $schemaMatch.Success) {
    throw "Could not extract schema block from root index.html"
}

$sharedSchema = $schemaMatch.Value.TrimEnd()

# All other index.html files except root homepage
$targetFiles = Get-ChildItem -Path $rootDir -Recurse -Filter "index.html" |
    Where-Object { $_.FullName -ne $sourceFile }

if (-not $targetFiles) {
    Write-Host "No other index.html files found." -ForegroundColor Yellow
    exit 0
}

foreach ($file in $targetFiles) {
    $html = Get-Content -Path $file.FullName -Raw -Encoding UTF8
    $originalHtml = $html

    # CASE 1: Page already has skip-link/header block before <main>
    if ($html -match '(?s)<a class="skip-link" href="#main-content">.*?(?=<main id="main-content">)') {
        $html = [regex]::Replace(
            $html,
            '(?s)<a class="skip-link" href="#main-content">.*?(?=<main id="main-content">)',
            $sharedHeader
        )
    }
    # CASE 2: Page has placeholder comments before <main>
    elseif ($html -match '(?s)<!-- Use your shared header/nav block from homepage -->.*?(?=<main id="main-content">)') {
        $html = [regex]::Replace(
            $html,
            '(?s)<!-- Use your shared header/nav block from homepage -->.*?(?=<main id="main-content">)',
            $sharedHeader
        )
    }
    else {
        Write-Host "Skipped header sync (pattern not found): $($file.FullName)" -ForegroundColor Red
    }

    # Replace existing JSON-LD schema block, or insert it before </head>
    if ($html -match $schemaPattern) {
        $html = [regex]::Replace(
            $html,
            $schemaPattern,
            $sharedSchema,
            1
        )
    }
    elseif ($html -match '</head>') {
        $html = [regex]::Replace(
            $html,
            '</head>',
            "`r`n  " + $sharedSchema + "`r`n</head>",
            1
        )
    }
    else {
        Write-Host "Skipped schema sync (no </head> tag found): $($file.FullName)" -ForegroundColor Red
    }

    # Replace everything after </main> with shared footer/tail
    if ($html -match '(?s)</main>.*?</html>\s*') {
        $html = [regex]::Replace(
            $html,
            '(?s)</main>.*?</html>\s*',
            "</main>`r`n`r`n" + $sharedFooter
        )
    }
    else {
        Write-Host "Skipped footer sync (no </main>...</html> pattern found): $($file.FullName)" -ForegroundColor Red
    }

    if ($html -ne $originalHtml) {
        Set-Content -Path $file.FullName -Value $html -Encoding UTF8
        Write-Host "Updated: $($file.FullName)" -ForegroundColor Green
    }
    else {
        Write-Host "No changes made: $($file.FullName)" -ForegroundColor Yellow
    }
}

Write-Host ""
Write-Host "Done. Shared header, schema, and footer synced from root index.html." -ForegroundColor Cyan
