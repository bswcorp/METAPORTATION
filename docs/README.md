
# METAPORTATION

Technical framework focused on modular architecture, smart contracts, and operational tooling.

## Overview

METAPORTATION is a modular development repository that contains smart contracts, internal modules, deployment scripts, and supporting utilities.  
The project is structured to support iterative development of on-chain components and related systems.

## Tech Stack

- **Smart Contracts**: Solidity
- **Runtime**: Node.js
- **Libraries**:
  - `ethers` v6
  - `web3`
  - `dotenv`
- **Scripts**: Python & Shell

## Getting Started

### Prerequisites

- Node.js (v18 or higher recommended)
- npm or yarn
- Python 3.x (for utility scripts)
- Solidity compiler (`solc`) if working with contracts

### Installation

```bash
git clone https://github.com/bswcorp/METAPORTATION.git
cd METAPORTATION
npm install
```

### Environment Setup

Create a `.env` file in the root directory:

```env
PRIVATE_KEY=your_private_key
RPC_URL=your_rpc_endpoint
```

## Repository Structure

```text
METAPORTATION/
├── contracts/                  # Smart contract source files
├── src/                        # Core application & deployment scripts
├── scripts/                    # Operational & utility scripts
├── modul-metaportasi/          # Core module
├── modul-psyche/               # Psyche module
├── modul-qubicoin/             # Qubicoin module
├── modul-quorum/               # Quorum module
├── modul-makronesia/           # Makronesia module
├── modul-solar-event/          # Solar event module
├── internal/
│   └── ALUTSISTA_REBORN/       # Internal components
├── docs/                       # Documentation
├── .github/workflows/          # CI/CD workflows
├── package.json
└── status & config files
```

## Detailed Module Structure

### 1. `contracts/`

Contains the main smart contract source files.

| File | Description |
|------|-------------|
| `TITAN-PSYCHE-MONO.sol` | Main monolithic contract |
| `TheGrandSovereignCore.sol` | Core contract logic |
| `supreme_contract.sol` | Supporting contract |

**Purpose:**
- On-chain business logic
- Vault-related functionality
- Deployable contract artifacts

### 2. `src/`

Core application files and deployment scripts.

| File | Description |
|------|-------------|
| `deploy.js` | Main deployment script |
| `stg_deploy_sovereign.js` | Sovereign deployment script |
| `index.html` | Frontend entry point |
| `gerbang_rahasia_19546.html` | Internal page |
| `tablet_wallpaper.html` | UI asset |
| `welcome_nasa.html` | Supporting page |

### 3. `scripts/`

Collection of utility scripts (Python & Shell) for deployment, monitoring, bridging, and system operations.

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

> **Note:** The `scripts/` folder currently contains a large number of operational files. It is recommended to reorganize them into subfolders (`deploy/`, `bridge/`, `monitoring/`, `utils/`) in the future for better maintainability.

### 4. Modular Folders

| Module | Path | Current Status | Intended Purpose |
|--------|----------------------|------------------|
| **modul-metaportasi** | `/modul-metaportasi` | Minimal files | Core Metaportation logic |
| **modul-psyche** | `/modul-psyche` | Contains `status.json` and `legacy_data/` | State / psyche related logic |
| **modul-qubicoin** | `/modul-qubicoin` | Minimal / empty | Token or coin related logic |
| **modul-quorum** | `/modul-quorum` | Minimal / empty | Consensus / quorum logic |
| **modul-makronesia** | `/modul-makronesia` | Minimal / empty | Makronesia related module |
| **modul-solar-event** | `/modul-solar-event` | Minimal / empty | Event handling module |

### 5. `internal/`

```text
internal/
└── ALUTSISTA_REBORN/     # Internal / experimental components
```

Used for internal development that is not yet fully exposed.

### 6. Root Configuration & Status Files

| File | Description |
|------|-------------|
| `metaport_status.json` | Current system status |
| `last_deploy_status.json` | Last deployment status |
| `collateral_manifest.json` | Collateral manifest |
| `global_migration_packet.json` | Migration data |
| `hasil_jembatan_likuiditas.json` | Liquidity bridge results |
| `PROKLAMASI_DIGITAL_STG.json` | Digital proclamation document |
| `package.json` | Project dependencies |

## Development Status

- [x] Core repository structure
- [x] Smart contract prototypes
- [x] Basic deployment scripts
- [x] Operational utility scripts
- [ ] Module completion (most modules still minimal)
- [ ] Test coverage
- [ ] Full documentation
- [ ] Production-ready deployment pipeline

## Recommended Future Structure (Optional)

To improve maintainability, the following structure is recommended:

```text
modules/
├── core/                 # modul-metaportasi
├── psyche/
├── qubicoin/
├── quorum/
├── makronesia/
└── solar-event/

contracts/
├── core/
├── vault/
└── interfaces/

scripts/
├── deploy/
├── bridge/
├── monitoring/
└── utils/
```

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/your-feature`)
3. Commit your changes
4. Push to the branch
5. Open a Pull Request

## License

This project is currently under active development.  
License information will be added in a future update.

## Maintainer

**Andi M. Harpianto**  
BSWCORP
```

---

