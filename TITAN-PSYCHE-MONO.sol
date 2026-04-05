// SPDX-License-Identifier: MIT
pragma solidity ^0.8.20;

/**
 * @title STG_Sovereign_Data_Vault
 * @dev Mengunci data tambang 16 Psyche & RIPE Atlas Probes secara Berdaulat.
 * Sultan WBP - 2026-2029
 */
contract STGSovereignVault {
    address public commander;
    
    struct MiningBlock {
        uint256 timestamp;
        string dataHash;
        string probeStatus;
    }

    MiningBlock[] public ledger;

    event BlockAnchored(uint256 timestamp, string dataHash);

    constructor() {
        commander = msg.sender;
    }

    modifier onlyCommander() {
        require(msg.sender == commander, "Bukan Hak Milik Anda!");
        _;
    }

    function anchorData(string memory _hash, string memory _probes) public onlyCommander {
        ledger.push(MiningBlock(block.timestamp, _hash, _probes));
        emit BlockAnchored(block.timestamp, _hash);
    }

    function getTotalBlocks() public view returns (uint256) {
        return ledger.length;
    }
}
