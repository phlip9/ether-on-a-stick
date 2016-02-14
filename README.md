Private network:
---

Philip:
    ip: 10.21.46.57

node01: enode://59aeee03f70774d53b159d9dc78fdab2ac9edfb804819a0659cd6ae9572f638c78cc51700c13f8e324fed2c2fd2aff4e683eb6f76415865c78ef50ee4f574002@[::]:30303
node02: enode://801688c5d686d216da9651acf471ab705fdd1b923f5aaaa3e30a3156660b658379ce666d9b54faa27a733f6f96826ca99b21e4d0632e7d99eb320ec1227e168f@[::]:30304
```bash
geth --networkid 5106293264 --genesis ./genesis.json --datadir="/tmp/eth/01" --nodiscover --ipcdisable --port 30303 --rpcport 8103 console
geth --networkid 5106293264 --genesis ./genesis.json --datadir="/tmp/eth/02" --nodiscover --ipcdisable --port 30304 --rpcport 8104 console
```

Max:
    ip: 10.21.45.138
    enode: enode://acb3a087e1692542a7f5d6a886779b6b344fd43be8a972b9ad17d152e3775ba5aa931c6ce3a1226145468c9a1237beb5044b13ba5ab10fc30cf8751363e50ac2@[::]:30303

Python
---

Morden:

`pyethapp --profile morden --data-dir ./.morden run --console`

Main:

`pyethapp --data-dir ./.main run --console`

Accounts:
---

Philip:
    account:
        01: 0x60aa0bbfbf7618be7289e29d07e7e7cc77d98238
        02: 0x07aace51f959d00b40c0cf6e26043aa830327ffb
    txn:
        01: {
            from: "0x07aace51f959d00b40c0cf6e26043aa830327ffb",
            to: "0x229d136fff6a7522a6ec49236f7005e45ded8325",
            value: 10.0 ether,
            id: "0xa03f876994fab5a2a5686a3702d93b3adf1874d09f95f4bb7e71ba4d48621f4d"
        }
Max:
    account:
        01: 0x229d136fff6a7522a6ec49236f7005e45ded8325


geth testnet:
---

```
geth --testnet --identity ethphlip --datadir="/tmp/eth/test01" --ipcdisable --port 30303 --rpcport 8103 --verbosity "0" console

geth --testnet --datadir="/tmp/eth/test01" account list

geth --testnet --datadir="/tmp/eth/test01" --unlock "0x60aa0bbfbf7618be7289e29d07e7e7cc77d98238"
```
