const ethers = require("ethers");
const fs = require("fs");

async function main() {
    // 1. Ganti dengan URL dari Alchemy/Infura Anda
    const provider = new ethers.providers.JsonRpcProvider("ISI_URL_ALCHEMY_ANDA_DI_SINI");
    
    // 2. Ganti dengan Private Key Dompet Anda (Gunakan dompet baru/kosong untuk keamanan!)
    const privateKey = "ISI_PRIVATE_KEY_ANDA_DI_SINI";
    const wallet = new ethers.Wallet(privateKey, provider);

    const abi = fs.readFileSync("./TITAN_PSYCHE_MONO_sol_TITAN_PSYCHE_MONO.abi", "utf8");
    const binary = fs.readFileSync("./TITAN_PSYCHE_MONO_sol_TITAN_PSYCHE_MONO.bin", "utf8");

    const factory = new ethers.ContractFactory(abi, binary, wallet);
    console.log("[STG] Deploying Sovereign Contract... Please wait.");
    
    const contract = await factory.deploy();
    await contract.deployed();

    console.log(`[SUCCESS] Contract Deployed at Address: ${contract.address}`);
}

main().catch((error) => {
    console.error(error);
    process.exit(1);
});
