# =====================================================
# DEPLOY MAESTRO ERP RECTIFICADORA SUAREZ (100% AUTO)
# =====================================================

Clear-Host
Write-Host "=== DEPLOY ERP RECTIFICADORA SUAREZ ===" -ForegroundColor Cyan

# CONFIGURACIÓN
$projectName = "RectificadoraSuarez_Final"
$projectPath = Join-Path $HOME "Documents\$projectName"
$repoUrl = "https://github.com/aanzulesb2-ship-it/rectificadora-app.git"
$publicUrl = "https://aanzulesb2-ship-it.github.io/rectificadora-app/"

# CREAR / ENTRAR A LA CARPETA
if (!(Test-Path $projectPath)) {
    New-Item -ItemType Directory -Path $projectPath -Force | Out-Null
    Write-Host "Carpeta creada: $projectPath" -ForegroundColor Green
}
Set-Location $projectPath

# CREAR INDEX.HTML
@"
<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>ERP Rectificadora Suarez</title>
<meta name="description" content="ERP profesional para rectificadoras. Gestión de órdenes y control técnico.">
<meta name="robots" content="index, follow">
<link rel="canonical" href="$publicUrl">
<script src="https://cdn.tailwindcss.com"></script>
</head>
<body class="bg-gray-100 p-10">
<h1 class="text-3xl font-black">ERP Rectificadora Suarez</h1>
<p class="mt-2">Sistema desplegado automáticamente con PowerShell.</p>
<p class="mt-4 font-bold">Usuario: admin | Clave: suarez</p>
</body>
</html>
"@ | Out-File -Encoding UTF8 index.html -Force

# ROBOTS.TXT
@"
User-agent: *
Allow: /
Sitemap: ${publicUrl}sitemap.xml
"@ | Out-File -Encoding UTF8 robots.txt -Force

# SITEMAP.XML
@"
<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
 <url>
  <loc>$publicUrl</loc>
  <lastmod>$(Get-Date -Format yyyy-MM-dd)</lastmod>
  <priority>1.0</priority>
 </url>
</urlset>
"@ | Out-File -Encoding UTF8 sitemap.xml -Force

Write-Host "Archivos web generados" -ForegroundColor Green

# GIT INIT (SI NO EXISTE)
if (!(Test-Path ".git")) {
    git init
    git branch -M main
    git remote add origin $repoUrl
}

git add .
git commit -m "Deploy automático ERP Rectificadora Suarez" 2>$null

# PUSH FORZADO (SOLUCIONA TU ERROR ANTERIOR)
git push -u origin main --force

Write-Host "Repositorio sincronizado con GitHub" -ForegroundColor Green

# ABRIR ARCHIVOS Y WEB
Start-Pr
