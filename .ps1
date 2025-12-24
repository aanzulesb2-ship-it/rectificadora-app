Clear-Host
Write-Host "=== DEPLOY ERP RECTIFICADORA SUAREZ (SUPABASE) ===" -ForegroundColor Cyan

# =========================
# CONFIGURACIÓN
# =========================
$projectName = "RectificadoraSuarez_Final"
$projectPath = "$HOME\Documents\$projectName"
$indexFile   = Join-Path $projectPath "index.html"

# 🔴 PEGA AQUÍ TUS CREDENCIALES SUPABASE
$supabaseUrl = "https://igjaxobidxuiuokotmgx.supabase.co"
$supabaseKey = "sb_publishable_mhmF6Re7HzkkQw-koUJ2bA_ThNnAfcW"

if ($supabaseUrl -like "PEGA*" -or $supabaseKey -like "PEGA*") {
    Write-Host "❌ ERROR: Debes pegar tus credenciales de Supabase en el script." -ForegroundColor Red
    exit
}

# =========================
# CREAR CARPETA
# =========================
if (!(Test-Path $projectPath)) {
    New-Item -ItemType Directory -Path $projectPath | Out-Null
}

Set-Location $projectPath

# =========================
# HTML + SUPABASE
# =========================
$html = @"
<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="UTF-8">
<title>ERP Rectificadora Suarez</title>
<script src="https://cdn.tailwindcss.com"></script>
<script src="https://cdn.jsdelivr.net/npm/@supabase/supabase-js@2"></script>
</head>
<body class="bg-gray-100 p-6">

<h1 class="text-3xl font-black mb-6">ERP Rectificadora Suarez</h1>

<div class="bg-white p-4 rounded shadow mb-4">
<input id="cliente" placeholder="Cliente / Motor" class="border p-2 w-full mb-2">
<button onclick="guardar()" class="bg-black text-white px-4 py-2 rounded">Guardar Orden</button>
</div>

<div id="lista" class="space-y-2"></div>

<script>
const supabase = supabaseJs.createClient(
  "$supabaseUrl",
  "$supabaseKey"
);

async function cargar() {
  const { data } = await supabase
    .from("orders")
    .select("*")
    .order("created_at", { ascending: true });

  const lista = document.getElementById("lista");
  lista.innerHTML = "";

  data.forEach(o => {
    lista.innerHTML += `
      <div class="bg-white p-3 rounded shadow flex justify-between">
        <span>\${o.client}</span>
        <span class="text-xs text-gray-400">\${o.status}</span>
      </div>
    `;
  });
}

async function guardar() {
  const cliente = document.getElementById("cliente").value;
  if (!cliente) return;

  await supabase.from("orders").insert({
    client: cliente,
    status: "pendiente"
  });

  document.getElementById("cliente").value = "";
  cargar();
}

cargar();
</script>

</body>
</html>
"@

$html | Out-File -Encoding utf8 -Force $indexFile
Write-Host "✔ Archivo index.html generado" -ForegroundColor Green

# =========================
# GIT
# =========================
if (!(Test-Path ".git")) {
    git init
    git branch -M main
}

git add .
git commit -m "Integracion Supabase ERP Suarez" | Out-Null
git push

Write-Host "✔ Repositorio actualizado en GitHub" -ForegroundColor Green

# =========================
# ABRIR PROYECTO
# =========================
Start-Process $indexFile
Start-Process "https://aanzulesb2-ship-it.github.io/rectificadora-app/"

Write-Host "=== DEPLOY COMPLETADO CON EXITO ===" -ForegroundColor Cyan
