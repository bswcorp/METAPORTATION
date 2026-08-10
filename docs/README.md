# METAPORTATION

Technical framework focused on modular architecture, smart contracts, and spatial computation utilities.

## Overview

METAPORTATION is a modular development repository that contains smart contracts, internal modules, scripts, and supporting tools.  
The project is structured to support iterative development of on-chain components and related utilities.

## Repository Structure

```text
METAPORTATION/
├── contracts/                  # Smart contract source files
├── src/                        # Main application / core logic
├── scripts/                    # Deployment and utility scripts
├── modul-psyche/               # Psyche-related module
├── modul-metaportasi/          # Core metaportasi module
├── modul-qubicoin/             # Qubicoin module
├── modul-quorum/               # Quorum module
├── modul-makronesia/           # Makronesia module
├── modul-solar-event/          # Solar event module
├── internal/
│   └── ALUTSISTA_REBORN/       # Internal experimental components
├── docs/                       # Documentation
├── .github/workflows/          # CI/CD workflows
├── package.json
└── ...

---

## Detailed Module Structure

### 1. `contracts/`
Berisi source code smart contract utama.

| File | Keterangan |
|------|----------|
| `TITAN-PSYCHE-MONO.sol` | Contract utama (monolithic) |
| `TheGrandSovereignCore.sol` | Core contract |
| `supreme_contract.sol` | Contract pendukung |

**Fungsi utama:**
- Logic on-chain
- Vault / sovereign related functionality
- Deployable contract artifacts

---

### 2. `src/`
Berisi file inti aplikasi dan deployment script.

| File | Keterangan |
|------|----------|
| `deploy.js` | Script deployment utama |
| `stg_deploy_sovereign.js` | Script deployment khusus sovereign |
| `index.html` | Frontend entry point |
| `gerbang_rahasia_19546.html` | Halaman internal |
| `tablet_wallpaper.html` | Asset/UI terkait |
| `welcome_nasa.html` | Halaman pendukung |

---

### 3. `scripts/`
Kumpulan utility script (Python & Shell) untuk operasional, deployment, monitoring, dan integrasi.

**Kategori Script:**

#### A. Deployment & Contract Related
- `deploy_metaport.py`
- `deploy_metaport_patched.py`
- `deploy_metaport_sovereign.py`
- `stg_web5_deployer.py`
- `stg_web5_deployer_final.py`
- `cek_kontrak_stg.py`
- `cek_gas_trust.py`

#### B. Bridge & Liquidity
- `bridge.py`
- `stg_bridge.py`
- `stg_bridge_export.py`
- `jembatan_likuiditas.py`
- `liquidity_bridge.py`
- `tarik_likuiditas.py`

#### C. Core System & Monitoring
- `stg_core.py`
- `main_command.py`
- `stg_shell.py`
- `mmgetstatus_stg.py`
- `reality_checker.py`
- `dormant_scanner.py`
- `sonar_gas_recovery.py`

#### D. Integration & Data
- `ambil_data_nasa.py`
- `stg_nasa_integrator.py`
- `injeksi_riset_nasa.py`
- `global_itinerary.py`
- `mapping_nusantara.py`

#### E. Utility & Maintenance
- `stg_autolinter.sh`
- `stg_integrator.sh`
- `Compile_curriculum.sh`
- `stg_precise_patcher.py`
- `patch_kedaulatan.py`

> Catatan: Folder `scripts/` berisi banyak file operasional. Disarankan mengelompokkan ulang ke subfolder (`deploy/`, `bridge/`, `monitoring/`, `utils/`) di masa depan agar lebih rapi.

---

### 4. Modular Folders

| Module | Path | Status / Isi Saat Ini | Fungsi yang Diharapkan |
|--------|------|-----------------------|-------------------------|
| **modul-metaportasi** | `/modul-metaportasi` | Masih minim file | Modul inti logika Metaportation |
| **modul-psyche** | `/modul-psyche` | Berisi `status.json` + `legacy_data/` | Modul terkait state / psyche logic |
| **modul-qubicoin** | `/modul-qubicoin` | Masih kosong / minim | Modul terkait tokenomics / coin logic |
| **modul-quorum** | `/modul-quorum` | Masih kosong / minim | Modul konsensus / quorum |
| **modul-makronesia** | `/modul-makronesia` | Masih kosong / minim | Modul terkait makronesia |
| **modul-solar-event** | `/modul-solar-event` | Masih kosong / minim | Modul event / solar related |

---

### 5. `internal/`

```text
internal/
└── ALUTSISTA_REBORN/     # Komponen internal / experimental
