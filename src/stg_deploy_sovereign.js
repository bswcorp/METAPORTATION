const Web3 = require('web3');
const fs = require('fs');

const web3 = new Web3(new Web3.providers.HttpProvider("http://127.0.0.1:8545"));

console.log("🏛️  [STG-DEPLOY] MENGGUNAKAN MESIN PURBA V0.20 (STABIL)...");

const abi = JSON.parse(fs.readFileSync("TITAN-PSYCHE-MONO_sol_STGSovereignVault.abi", "utf8"));
const binData = fs.readFileSync("TITAN-PSYCHE-MONO_sol_STGSovereignVault.bin", "utf8").trim();
const bytecode = binData.startsWith('0x') ? binData : '0x' + binData;

const admin = web3.eth.accounts[0];
console.log("[STG-SYSTEM] Akun Panglima:", admin);

const SovereignContract = web3.eth.contract(abi);

console.log("[STG-DEPLOY] Menanam Kedaulatan di Ganache...");

SovereignContract.new({
    from: admin,
    data: bytecode,
    gas: 4700000
}, function (e, contract) {
    if (e) {
        console.error("❌ [STG-ERROR]", e);
        return;
    }

    if (typeof contract.address !== 'undefined') {
        console.log("==================================================");
        console.log("👑 KEDAULATAN AKTIF: TITAN-PSYCHE-MONO");
        console.log("Alamat Kontrak:", contract.address);
        console.log("==================================================");

        const status = {
            address: contract.address,
            deployer: admin,
            timestamp: new Date().toISOString()
        };
        fs.writeFileSync("last_deploy_status.json", JSON.stringify(status, null, 4));
        process.exit(0);
    }
});
