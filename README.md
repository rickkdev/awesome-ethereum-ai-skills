# ⟠ Awesome Ethereum & Web3 AI Skills

> A curated list of AI skills, MCP servers, and plugins for Ethereum and Web3 development. These give AI agents (Claude, ChatGPT, Cursor, OpenClaw, etc.) the ability to interact with blockchains, write smart contracts, trade tokens, query on-chain data, and more.

Project tables include a linked **Last GitHub commit** date. See [freshness and maintenance](#freshness-and-maintenance) for the snapshot date, scope, and refresh command.

> [!WARNING]
> **None of the skills or MCP servers listed here have been audited.** This is a community-compiled directory of projects shared on social media, listed on skill hubs, and found across public repositories. We make no guarantees about their safety, integrity, or intentions. Exercise extreme caution with anything that touches wallets, private keys, seed phrases, or transaction signing — a malicious skill can compromise your agent and drain your funds. Always review the source code, verify the authors, and do your own research (DYOR) before installing or granting permissions to any skill or MCP server.

---

## 📑 Contents

- [🎓 General Knowledge](#-general-knowledge)
- [🔌 Protocol-Specific Skills & Plugins](#-protocol-specific-skills--plugins)
- [📈 Exchange & Trading Skills](#-exchange--trading-skills)
- [🛡️ Smart Contract Security](#️-smart-contract-security)
- [📊 DeFi Data & Analytics](#-defi-data--analytics)
- [⛓️ Chain-Specific MCP Servers](#️-chain-specific-mcp-servers)
- [💱 Trading & DeFi MCP Servers](#-trading--defi-mcp-servers)
- [📉 Market Data MCP Servers](#-market-data-mcp-servers)
- [🌉 Cross-Chain & Bridge MCP Servers](#-cross-chain--bridge-mcp-servers)
- [👛 Wallet & Infrastructure](#-wallet--infrastructure)
- [📚 Education](#-education)
- [🗂️ Awesome Lists & Directories](#️-awesome-lists--directories)
- [🔍 Discovery Resources](#-discovery-resources)
- [Freshness and maintenance](#freshness-and-maintenance)

---

## 🎓 General Knowledge

> Foundational Ethereum and crypto knowledge packaged as AI skills.

| Name | Description | Link | Last GitHub commit |
| --- | --- | --- | --- |
| **ETHSKILLS** | The most important skill you need to have. Modular Ethereum knowledge for AI agents — gas, L2s, standards, security, DeFi, auditing, and more. No install required. Built by Austin Griffith / BuidlGuidl / Ethereum Foundation. | [ethskills.com](https://ethskills.com/) · [Source](https://github.com/austintgriffith/ethskills) | [2026-08-20](https://github.com/austintgriffith/ethskills/commit/06ea4efa08076ff04f6ca4945ef4a2ca881115b0) |
| **CryptoSkills** | 97+ production-ready AI agent skills across 14 categories and 15 blockchains. Covers DeFi protocols (Aave, Compound, Curve, Lido, Pendle, GMX, etc.), L2s (Arbitrum, Base, Optimism, StarkNet, etc.), oracles (Chainlink, Pyth, RedStone), security tools, cross-chain bridges, dev frameworks, and more. Install via `npx cryptoskills install`. | [cryptoskills.dev](https://cryptoskills.dev/) · [Source](https://github.com/andresdefi/cryptoskills) | [2026-03-09](https://github.com/andresdefi/cryptoskills/commit/61953379563a83c27e3140e4c875015e7ccf4312) |
| **kukapay/crypto-skills** | Collection of specialized AI agent skills — EVM Swiss Knife, Market Sentiment, Meme Scout, Token Minter, Trading Strategist, Yield Opportunities. Install via `npx skills add kukapay/crypto-skills`. | [GitHub](https://github.com/kukapay/crypto-skills) | [2026-05-04](https://github.com/kukapay/crypto-skills/commit/868a437f8dcb8ce72669a5a67dd6a016951ef29a) |
| **crypto-agent-skill** | Real-time crypto market data skill built with the agentskills.io open standard. | [GitHub](https://github.com/JStrait515/crypto-agent-skill) | [2026-02-20](https://github.com/JStrait515/crypto-agent-skill/commit/4b487436901fd0c1c26a1d3cc7e75ce51ed431fb) |

## 🔌 Protocol-Specific Skills & Plugins

| Name | Protocol/Focus | Description | Link | Last GitHub commit |
| --- | --- | --- | --- | --- |
| **Uniswap AI** | Uniswap | Swap integration, pay-with-any-token (x402/MPP), and v4 hook development. Works with Claude Code, MCP, and Skills CLI. | [GitHub](https://github.com/Uniswap/uniswap-ai) | [2026-09-29](https://github.com/Uniswap/uniswap-ai/commit/1a43e968a39537d5a73aeca20dd1ed9d96f502fa) |
| **OpenZeppelin Skills** | OpenZeppelin Contracts | Authoritative knowledge of audited smart contract libraries across Solidity, Cairo, Stylus, and Stellar. Covers tokens, access control, governance, and security primitives. | [openzeppelin.com](https://www.openzeppelin.com/news/introducing-openzeppelin-skills) · [Source](https://github.com/OpenZeppelin/openzeppelin-skills/tree/main/skills) | [2026-07-15](https://github.com/OpenZeppelin/openzeppelin-skills/commit/6f215af60eb60017ab1a933ce9d22a479cd42b26) |
| **OpenZeppelin Contracts MCP** | OpenZeppelin Contracts | Hosted MCP servers for generating contracts with OpenZeppelin libraries. | [mcp.openzeppelin.com](https://mcp.openzeppelin.com/) · [Source](https://github.com/OpenZeppelin/openzeppelin-mcp) | [2026-09-09](https://github.com/OpenZeppelin/openzeppelin-mcp/commit/10e51d99b5317550fb70c715d016665485699679) |
| **UCAI** | Any EVM Contract | Universal Contract AI Interface — generates MCP servers from any ABI. One command to make every function callable by Claude. Supports Uniswap, Aave, ERC20s, NFTs. | [GitHub](https://github.com/nirholas/UCAI) | [2026-10-09](https://github.com/nirholas/UCAI/commit/c25ecc5f400225464f1cdd0562ca51e5505ed00d) |
| **DeFi Rates MCP** | Aave, Morpho, Compound, etc. | Real-time DeFi lending rates across 13+ protocols. | [GitHub](https://github.com/qingfeng/defi-rates-mcp) | [2026-05-09](https://github.com/qingfeng/defi-rates-mcp/commit/76bccc94cafcbb88ce1a36b4eb9c9cb37ff0b279) |
| **Chainlink Feeds MCP** | Chainlink | Real-time access to Chainlink's decentralized price feeds on Ethereum, Base, and more. | [mcplane.com](https://www.mcplane.com/mcp_servers/chainlink-feeds) | Not verified |
| **Alchemy Skills** | Alchemy (Multi-chain) | Agent Skills for all Alchemy products — EVM JSON-RPC, Token API, NFT API, Prices API, Portfolio API, Webhooks. Supports API key, x402, and MPP access. Install via `npx skills add alchemyplatform/skills -g --yes`. | [GitHub](https://github.com/alchemyplatform/skills) | [2026-08-26](https://github.com/alchemyplatform/skills/commit/4caf3e555c3af8dbb9e5b540aed558aef986d885) |
| **Arbitrum dApp Skill** | Arbitrum | Claude Code skill for scaffolding complete Arbitrum dApps — Stylus Rust + Solidity contracts, React frontends, local devnode, deployment to Sepolia/One. | [GitHub](https://github.com/hummusonrails/arbitrum-dapp-skill) | [2026-06-02](https://github.com/hummusonrails/arbitrum-dapp-skill/commit/92338a186e8974ccb308d2226536c88df381bee7) |
| **Hyperlane MCP** | Hyperlane | Interoperability tooling for interchain AI agents. | [hyperlane.xyz](https://www.hyperlane.xyz/post/introducing-hyperlane-mcp-tooling-for-interchain-agents) | Not verified |
| **Brian API** | Natural Language → Web3 | Converts natural language to Web3 transactions. | [brian.so](https://www.brian.so/) | Not verified |
| **Rocket Pool Skills** | Rocket Pool | Ethereum staking skills with contract addresses, ABIs, and Foundry `cast` examples. Includes an all-in-one bundle and separate staking, node, governance, and rewards bundles. | [Skill bundle](https://github.com/rocket-pool/skills/tree/main/all-in-one) · [All skills](https://github.com/rocket-pool/skills) | [2026-08-18](https://github.com/rocket-pool/skills/commit/af5ed497e4d3d153f44334231909912222e14052) |
| **Across Skills** | Across | Cross-chain bridge and swap integration skills covering quotes, embedded destination-chain actions, and deposit tracking. | [Skills](https://github.com/across-protocol/skills/tree/master/skills) | [2026-02-27](https://github.com/across-protocol/skills/commit/2b0ffd11824e3c97682ddb491c4ad141c4e0f5d0) |
| **OpenSea Skills** | OpenSea / Seaport | Skills for NFT data, Seaport trading, ERC-20 swaps, wallet setup, and gated agent tools on Base. Public release mirror can lag internal development. | [GitHub](https://github.com/ProjectOpenSea/opensea-skill) · [SKILL.md](https://github.com/ProjectOpenSea/opensea-skill/blob/main/SKILL.md) | [2026-10-06](https://github.com/ProjectOpenSea/opensea-skill/commit/42418c8dc305784bd67bb19e39796d37eb3bafc4) |
| **1inch AI** | 1inch | Agent skills and hosted MCP configuration for swaps, limit orders, market data, wallet data, and SDK documentation. | [Skills](https://github.com/1inch/1inch-ai/tree/main/skills) | [2026-09-13](https://github.com/1inch/1inch-ai/commit/11126423d43d5d67c378ac80450850f5536e2b34) |
| **Build on Base Skill** | Base | Skill for building apps and deploying contracts on Base, with task-specific references. | [Skill](https://github.com/base/skills/tree/master/skills/build-on-base) | [2026-09-17](https://github.com/base/skills/commit/15adb8d9c75e5c7d1461e183a9021170a6ddbc08) |

## 📈 Exchange & Trading Skills

| Name | Platform | Description | Link | Last GitHub commit |
| --- | --- | --- | --- | --- |
| **Binance AI Agent Skills** | Binance | 11 modular skills for spot trading, derivatives, margin, market intelligence, token auditing, asset management, and Binance Alpha data. | [binance.com](https://www.binance.com/en/support/announcement/detail/bafb9dda6cbb47d5882a4090c31d4c64) · [Source](https://github.com/binance/binance-skills-hub/tree/main/skills) | [2026-09-11](https://github.com/binance/binance-skills-hub/commit/eaede5893f1a52ec4c31aacec686e9854c79d790) |
| **Bybit AI Skills** | Bybit | 253 API endpoints — market intelligence, spot trading, derivatives, earn products, account management. Works with ChatGPT, Claude, OpenClaw, Cursor. | [GitHub](https://github.com/bybit-exchange/skills) | [2026-10-13](https://github.com/bybit-exchange/skills/commit/0339e6bf160865f9089b6f1e0a52076ff141d672) |

## 🛡️ Smart Contract Security

| Name | Focus | Description | Link | Last GitHub commit |
| --- | --- | --- | --- | --- |
| **ETHSKILLS Audit** | Solidity | 500+ item contract audit system with specialist agents. | [ethskills.com](https://ethskills.com/) · [Source](https://github.com/austintgriffith/ethskills/tree/master/audit) | [2026-02-28](https://github.com/austintgriffith/ethskills/commit/4d19220b19da0f8f0e1b344ab60679e4a096f098) |
| **pashov/skills** ⭐ | Solidity | Solidity audit skill from Pashov Audit Group — `solidity-auditor` folder delivers sub-5-minute security feedback on Solidity code changes. Install with `Install skill https://github.com/pashov/skills/`, then run `run solidity auditor on the codebase`. Ideal for real-time auditing while coding. | [GitHub](https://github.com/pashov/skills) | [2026-10-05](https://github.com/pashov/skills/commit/92b0ea6786e6c210bc9a839e4813d50876c1c550) |
| **Cyfrin/solskill** | Solidity | Solidity security development skill from the Cyfrin audit team. | [GitHub](https://github.com/Cyfrin/solskill) | [2026-06-18](https://github.com/Cyfrin/solskill/commit/d17bda028df073c61711a1fe156b5ca5dea91642) |
| **QuillShield** | Solidity | AI-powered vulnerability detection that learns from past exploits, reduces false positives. | [Github](https://github.com/quillai-network/quillshield_skills) | [2026-03-30](https://github.com/quillai-network/quillshield_skills/commit/8bdd3c058704cd855ce29b8e2385708b59152606) |
| **kadenzipfel/scv-scan** | Solidity | SCV Scan — Solidity vulnerability scanning skill. | [GitHub](https://github.com/kadenzipfel/scv-scan) | [2026-03-11](https://github.com/kadenzipfel/scv-scan/commit/114985581450cfed35c277831a065c6478e2c328) |
| **Archethect/sc-auditor** | Solidity | Smart contract security auditor skill. | [GitHub](https://github.com/Archethect/sc-auditor) | [2026-03-13](https://github.com/Archethect/sc-auditor/commit/942cc13111cf5b0617d9de8fa4fe9bc20f1d8cc8) |
| **auditmos/skills** | Solidity | Security audit skills from the Auditmos team. | [GitHub](https://github.com/auditmos/skills) | [2025-12-30](https://github.com/auditmos/skills/commit/c958b3abb0ce189d9f39a05caf94b5a5da655010) |
| **zerocoolailabs/ZeroSkills** | Solidity | Vulnerability detector skill for Solidity contracts. | [GitHub](https://github.com/zerocoolailabs/ZeroSkills) | [2026-08-11](https://github.com/zerocoolailabs/ZeroSkills/commit/026efbe622930d86a3d2c2a520523e89bd02ebf7) |
| **marchev/claudit** | Solidity | Security findings skill for smart contract auditing. | [GitHub](https://github.com/marchev/claudit) | [2026-04-23](https://github.com/marchev/claudit/commit/b9f0372926a58e476bba47db57af6c6934c356fb) |
| **ZealynxSecurity/krait** | Solidity | AI-first smart contract security auditor from ZealynxSecurity. | [GitHub](https://github.com/ZealynxSecurity/krait) | [2026-08-11](https://github.com/ZealynxSecurity/krait/commit/76e5ac7b74ce5517409870c2974e6baaddc8f99e) |
| **trailofbits/skills** | Multi-Lang | Security dev testing skills from Trail of Bits — creators of Slither, Echidna, and Manticore. | [GitHub](https://github.com/trailofbits/skills) | [2026-10-14](https://github.com/trailofbits/skills/commit/0f44fe01dcb00bd6929b4ba82a257d305de04554) |
| **JoranHonig/grimoire** | Multi-Lang | Co-auditor skill from Ethereum security researcher Joran Honig. | [GitHub](https://github.com/JoranHonig/grimoire) | [2026-10-13](https://github.com/JoranHonig/grimoire/commit/360d764982807882d3e5834fd4197727df91f81a) |
| **forefy/.context** | Multi-Lang | Security audit skills from Forefy. | [GitHub](https://github.com/forefy/.context) | [2026-10-04](https://github.com/forefy/.context/commit/c8ff161fccdeef9a0416df6230636eb2dfde4a8b) |
| **0xiehnnkta/nemesis-auditor** | Multi-Lang | Nemesis security audit agent skill. | [GitHub](https://github.com/0xiehnnkta/nemesis-auditor) | [2026-03-16](https://github.com/0xiehnnkta/nemesis-auditor/commit/75cecc6dbd798f82ed8928d1a906078be9c575de) |
| **Monethic/monethic-maia** | Multi-Lang | AI auditor skill from Monethic. | [GitHub](https://github.com/Monethic/monethic-maia) | [2026-03-27](https://github.com/Monethic/monethic-maia/commit/80c6fd7b3045dfce1a6836480deb50e84ee5ec69) |
| **hackenproof-public/skills** | Web3 Security | Bug triage skills from HackenProof's Web3 security platform. | [GitHub](https://github.com/hackenproof-public/skills) | [2026-09-07](https://github.com/hackenproof-public/skills/commit/60d88130e42a24d4678b636efdcd7af846c990db) |
| **EVM MCP Tools** | EVM | Blockchain analysis toolkit for Claude — audit smart contracts, analyze wallets, track profitability, fetch on-chain data via MCP. | [GitHub](https://github.com/0xGval/evm-mcp-tools) | [2025-03-25](https://github.com/0xGval/evm-mcp-tools/commit/b2f05e0f5fccb4453b3eb4779e7df72b2e125b5e) |
| **SecSkills Web3** | Web3 Security | Security-first Web3 development for Ethereum and EVM chains. | [LobeHub](https://lobehub.com/skills/trilwu-secskills-web3-blockchain) | Not verified |
| **Web3 Testing Skill** | Web3 Security | Smart contract testing workflow with Hardhat + Foundry — unit, integration, fuzzing, gas profiling, fork testing. Specially built for OpenClaw setups. | [LobeHub](https://lobehub.com/skills/agent-skills-hub-agent-skills-hub-web3-testing) | Not verified |
| **Slither MCP** | Solidity | Trail of Bits MCP server for Slither detectors, contract metadata, inheritance, and function call relationships. Supports Foundry and Hardhat projects. | [GitHub](https://github.com/trailofbits/slither-mcp) | [2026-02-13](https://github.com/trailofbits/slither-mcp/commit/17755731bf7aba6e5ed4d72e116d9d394430b1e2) |

## 📊 DeFi Data & Analytics

| Name | Focus | Description | Link | Last GitHub commit |
| --- | --- | --- | --- | --- |
| **Dune Analytics MCP** | On-chain data | Connects AI agents to Dune's data warehouse across 100+ blockchains. Query stablecoin flows, DEX volumes via natural language. | [GitHub](https://github.com/kukapay/dune-analytics-mcp) | [2025-05-04](https://github.com/kukapay/dune-analytics-mcp/commit/6425872d69ce545bffd9b0d1e998c0083be8acab) |
| **Dune CLI + Skills** | On-chain data | Official skills for querying blockchain data, discovering datasets, and managing queries through the Dune CLI. | [blockchain.news](https://blockchain.news/news/dune-analytics-agent-native-cli-skills-launch) · [Source](https://github.com/duneanalytics/skills/tree/main/skills/dune) | [2026-04-30](https://github.com/duneanalytics/skills/commit/bb0c9fcf0568ec10e4ca0190e2e0e3e0086958ea) |
| **Zerion MCP + Skills** | Portfolio & on-chain data | Connects Claude to on-chain data for portfolio analysis, wallet tracking, and DeFi research. | [zerion.io](https://zerion.io/blog/zerion-for-api-ai-agents-mcp-skills/) · [Source](https://github.com/zeriontech/zerion-ai/tree/main/skills/zerion) | [2026-10-06](https://github.com/zeriontech/zerion-ai/commit/488cdd0bbcf19ad08d30c79f99744a75008b2b92) |
| **The Graph MCP** | Indexed blockchain data | Query indexed blockchain data from The Graph's subgraphs. | [GitHub](https://github.com/kukapay/thegraph-mcp) | [2025-07-31](https://github.com/kukapay/thegraph-mcp/commit/2ee94eb3538dcbf4fde243c2f653949a74084e75) |
| **DeFi Llama MCP** | DeFi analytics | API wrapper around the DeFi Llama ecosystem for TVL, yield, and protocol data. | [GitHub](https://github.com/demcp/demcp-defillama-mcp) | [2025-05-15](https://github.com/demcp/demcp-defillama-mcp/commit/877ece7d957dd497cb00e8c51014295da080e439) |
| **Hive Intelligence** | Multi-chain | MCP server connecting AI agents to 60+ blockchains with real-time crypto data. Works with Claude, ChatGPT, LangChain. | [hiveintelligence.xyz](https://hiveintelligence.xyz/) | Not verified |
| **Codex MCP** | Multi-chain | Enriched blockchain data from Codex. | [GitHub](https://github.com/Codex-Data/codex-mcp) | [2025-04-05](https://github.com/Codex-Data/codex-mcp/commit/d31ebf35eef28d8f3bd57ad63fb13b9470849cbd) |
| **Web3 Research MCP** | Crypto research | Deep research for crypto — local analysis and research automation. | [GitHub](https://github.com/aaronjmars/web3-research-mcp) | [2026-10-14](https://github.com/aaronjmars/web3-research-mcp/commit/e0ebc38ece15d7b84cd45e349129abfa09ac83e0) |
| **DefiLlama Skills** | DeFi analytics | Official skills for DefiLlama's hosted MCP, including TVL, yields, protocol research, chain comparisons, and risk analysis. | [GitHub](https://github.com/DefiLlama/defillama-skills) | [2026-03-26](https://github.com/DefiLlama/defillama-skills/commit/f286bda4498ec8da4eb57bfba8ab40c188860e8e) |
| **Blockscout Analysis Skill** | EVM on-chain data | Guides agents using Blockscout MCP, including query strategy, API references, and response handling. | [Skill](https://github.com/blockscout/agent-skills/tree/main/blockscout-analysis) | [2026-06-17](https://github.com/blockscout/agent-skills/commit/971f8894b75207a48eeb6a7db3833047b9336d70) |
| **eth-labels MCP** | EVM address labels | Looks up Ethereum and EVM address labels, searches by project or token name, and reports dataset statistics. | [GitHub](https://github.com/dawsbot/eth-labels) | [2026-09-25](https://github.com/dawsbot/eth-labels/commit/d9b21aefeded56f7fce7208d6fa173d128526c1b) |

## ⛓️ Chain-Specific MCP Servers

| Name | Chain | Description | Link | Last GitHub commit |
| --- | --- | --- | --- | --- |
| **Base MCP (legacy)** | Base | Archived legacy server. Use the Wallet MCP Skill below for the current integration. | [GitHub](https://github.com/base/base-mcp-legacy) | [2026-05-13](https://github.com/base/base-mcp-legacy/commit/979dde3e32dc63081a40a533be84e6e848be25c9); archived |
| **Etherscan MCP** | Ethereum | Ethereum blockchain data tools via Etherscan API. | [GitHub](https://github.com/crazyrabbitLTC/mcp-etherscan-server) | [2024-12-31](https://github.com/crazyrabbitLTC/mcp-etherscan-server/commit/73578d9274f93ecf714f70b73c7c9d58a6453491) |
| **eth-mcp** | Ethereum | Direct Ethereum blockchain interaction. | [GitHub](https://github.com/0xKoda/eth-mcp) | [2025-04-01](https://github.com/0xKoda/eth-mcp/commit/706205455dbad82297dba2d3d83951e8ee9448fc) |
| **QuickNode EVM MCP** | Multi-EVM | Multichain RPC server (Ethereum, Arbitrum, Base, BSC) using Viem. | [quicknode.com](https://www.quicknode.com/guides/ai/evm-mcp-server) | Not verified |
| **evm-mcp-server** | Multi-EVM | Blockchain services across multiple EVM-compatible networks. | [GitHub](https://github.com/mcpdotdirect/evm-mcp-server) | [2026-06-04](https://github.com/mcpdotdirect/evm-mcp-server/commit/128ac3d4b1ea96084d55a9578306d017006e709d) |
| **Strangelove web3-mcp** | Multi-chain | "1 MCP to rule all them chains" — includes Ethereum and EVM chains. | [GitHub](https://github.com/amygdala-labs/web3-mcp) | [2025-03-18](https://github.com/amygdala-labs/web3-mcp/commit/1b9e5ce23c855503ff2c9f5fc63a737edbd81216) |
| **BSC MCP** | Binance Smart Chain | Token transfers and smart contract interaction on BSC. | [GitHub](https://github.com/TermiX-official/bsc-mcp) | [2025-08-30](https://github.com/TermiX-official/bsc-mcp/commit/a0aa570c672b412c347ce821d42d93e5432d2de5) |
| **Polygon MCP** | Polygon PoS | On-chain tools for Claude AI on Polygon. | [GitHub](https://github.com/Dablclub/polygon-mcp) | [2025-04-04](https://github.com/Dablclub/polygon-mcp/commit/8ef86cd8a8b023b75e3e3f10350dea70fcb95a3f) |
| **StarkNet MCP** | StarkNet | Query blockchain data, manage wallets, interact with smart contracts. | [GitHub](https://github.com/mcpdotdirect/starknet-mcp-server) | [2025-11-26](https://github.com/mcpdotdirect/starknet-mcp-server/commit/8fdd1be36efb7fd0c899086e68d3b9603cf7ade4) |
| **Alchemy SDK MCP** | Multi-chain | Integration with Alchemy SDK for blockchain and NFT operations. | [GitHub](https://github.com/itsanishjain/alchemy-sdk-mcp) | [2025-03-05](https://github.com/itsanishjain/alchemy-sdk-mcp/commit/6a99c46a7a28156124a75f4b69d1456aeca8d72f) |
| **Linea MCP** | Linea | On-chain tools for AI applications on Linea. | [GitHub](https://github.com/qvkare/linea-mcp) | [2026-01-15](https://github.com/qvkare/linea-mcp/commit/2e20fe26f7fce803e4eb3f954405925bd9cddbb4) |
| **Nodit MCP** | Multi-chain | Structured, context-ready blockchain data. | [GitHub](https://github.com/noditlabs/nodit-mcp-server) | [2026-06-23](https://github.com/noditlabs/nodit-mcp-server/commit/36cb42f43a4828ec49a49858e5b38516e3066473) |
| **Bankless Onchain MCP** | Multi-chain | Blockchain data interaction through the Bankless API. | [GitHub](https://github.com/Bankless/onchain-mcp) | [2026-05-05](https://github.com/Bankless/onchain-mcp/commit/f81f69a14560caf3394d0aeff0395958308e4fea) |
| **Web3 Agent MCP** | Multi-chain | Ethereum, Polygon, Arbitrum, Optimism, Base, Avalanche — DeFi protocol interactions (Aave, Balancer, Convex, Curve, GMX, Morpho). | [LobeHub](https://lobehub.com/mcp/whatl3y-web3-agent) | Not verified |
| **Foundry MCP Server** | Ethereum | Experimental MCP server for Foundry — built for Solidity devs. | [GitHub](https://github.com/PraneshASP/foundry-mcp-server) | [2026-01-17](https://github.com/PraneshASP/foundry-mcp-server/commit/3627242fa6c4dfff65322224bf6cdd29f42a92aa) |
| **Blockscout MCP** | Ethereum / EVM | Blockscout API tools for balances, transactions, tokens, NFTs, and verified contract metadata across EVM chains. | [GitHub](https://github.com/blockscout/mcp-server) | [2026-09-08](https://github.com/blockscout/mcp-server/commit/095ef2c03f1aa3325da0baa41c8bf29aa1bbb6e6) |

## 💱 Trading & DeFi MCP Servers

| Name | Focus | Description | Link | Last GitHub commit |
| --- | --- | --- | --- | --- |
| **Binance MCP** | Binance | Interact with Binance API. | [GitHub](https://github.com/TermiX-official/binance-mcp) | [2025-04-16](https://github.com/TermiX-official/binance-mcp/commit/93fb7f773580adb0417bdc4e436d88a542586dea) |
| **Uniswap Trader MCP** | Uniswap | Automate token swaps on Uniswap DEX. | [GitHub](https://github.com/kukapay/uniswap-trader-mcp) | [2025-05-07](https://github.com/kukapay/uniswap-trader-mcp/commit/b743a9d009491ed1132836217505ddb401d1cd1e) |
| **Uniswap PoolSpy MCP** | Uniswap | Track newly created liquidity pools on Uniswap (9 networks). | [GitHub](https://github.com/kukapay/uniswap-poolspy-mcp) | [2025-03-27](https://github.com/kukapay/uniswap-poolspy-mcp/commit/a4dfb09adf9cddaade5c6b2ce4ef45c44c2a4864) |
| **PancakeSwap PoolSpy MCP** | PancakeSwap | Track newly created liquidity pools. | [GitHub](https://github.com/kukapay/pancakeswap-poolspy-mcp) | [2025-05-07](https://github.com/kukapay/pancakeswap-poolspy-mcp/commit/533e34308f3cbf8528e079c76dd3a6b53d5c4d3d) |
| **Hyperliquid MCP** | Hyperliquid | Integrates the Hyperliquid SDK. | [GitHub](https://github.com/mektigboy/server-hyperliquid) | [2025-03-06](https://github.com/mektigboy/server-hyperliquid/commit/a7ee89e10d6d5b4dd58ef85c4aa6511cdc7132fb) |
| **DeFi Yields MCP** | Multi-protocol | Explore DeFi yield opportunities across protocols. | [GitHub](https://github.com/kukapay/defi-yields-mcp) | [2025-04-19](https://github.com/kukapay/defi-yields-mcp/commit/49292e436fe41625f80b5cc74a1fb81816ca2f5a) |
| **Bridge Rates MCP** | Cross-chain | Real-time cross-chain bridge rates. | [GitHub](https://github.com/kukapay/bridge-rates-mcp) | [2025-04-24](https://github.com/kukapay/bridge-rates-mcp/commit/8b75b09c48658baf30deae127e2bde4e07785c6b) |
| **Token Revoke MCP** | Multi-chain | Check and revoke ERC-20 token allowances. | [GitHub](https://github.com/kukapay/token-revoke-mcp) | [2025-03-28](https://github.com/kukapay/token-revoke-mcp/commit/6329892f519f25ee5160b1329f64314699a6a690) |
| **Token Minter MCP** | 21 chains | Mint ERC-20 tokens across 21 blockchains. | [GitHub](https://github.com/kukapay/token-minter-mcp) | [2025-04-28](https://github.com/kukapay/token-minter-mcp/commit/ab2e6adf0958ba7fdf89ce47f5a7197f571a1718) |
| **Free USDC Transfer MCP** | Base | Free USDC transfers on Base. | [GitHub](https://github.com/magnetai/mcp-free-usdc-transfer) | [2025-01-17](https://github.com/magnetai/mcp-free-usdc-transfer/commit/56a773dad543cc65f81c453fc6ff39e05d187442) |
| **Bybit MCP** | Bybit | Archived server for read-only access to the Bybit exchange API. | [GitHub](https://github.com/sammcj/bybit-mcp) | [2025-05-26](https://github.com/sammcj/bybit-mcp/commit/249395f6b8046bad5a1cc2fabb4eda127678e102); archived |
| **Freqtrade MCP** | Freqtrade | Integration with Freqtrade crypto trading bot. | [GitHub](https://github.com/kukapay/freqtrade-mcp) | [2025-12-06](https://github.com/kukapay/freqtrade-mcp/commit/6762093f9a294f770c886edcc1eda1c5a5ddeaf8) |
| **Bankr Skill** | Ethereum / Base / multi-chain | Bankr CLI and API skill for wallet queries, token transfers, swaps, and trading workflows. | [Skill](https://github.com/BankrBot/skills/tree/main/bankr) | [2026-10-12](https://github.com/BankrBot/skills/commit/80544ccb2429161264deca88156436368cc60305) |

## 📉 Market Data MCP Servers

| Name | Source | Description | Link | Last GitHub commit |
| --- | --- | --- | --- | --- |
| **CoinGecko MCP** | CoinGecko Pro | CoinGecko Pro API integration. | [GitHub](https://github.com/crazyrabbitLTC/mcp-coingecko-server) | [2025-06-11](https://github.com/crazyrabbitLTC/mcp-coingecko-server/commit/f47d0359a77060bf17229187eaad0a0a56bd7f3d) |
| **CoinMarketCap MCP** | CoinMarketCap | Real-time prices, market cap, and volume. | [GitHub](https://github.com/anjor/coinmarket-mcp-server) | [2025-06-24](https://github.com/anjor/coinmarket-mcp-server/commit/02343af289a81267701e2b14095b5bbc5585045b) |
| **CoinStats MCP** | CoinStats | Market data, portfolio tracking, and news. | [GitHub](https://github.com/CoinStatsHQ/coinstats-mcp) | [2026-10-13](https://github.com/CoinStatsHQ/coinstats-mcp/commit/7ae6fcc5db80b61cb672b42a68283c7310b802bd) |
| **CCXT MCP** | Major exchanges | Real-time and historical market data via CCXT. | [GitHub](https://github.com/Nayshins/mcp-server-ccxt) | [2025-02-17](https://github.com/Nayshins/mcp-server-ccxt/commit/f7ddee5eb4a335e42541e0c45c6785aa6c88591b) |
| **DexScreener MCP** | DexScreener | DEX pair data, token info, and market statistics. | [GitHub](https://github.com/openSVM/dexscreener-mcp-server) | [2025-01-06](https://github.com/openSVM/dexscreener-mcp-server/commit/4d24cbf156ff015ccbf5ac6bba554a523ac6335b) |
| **Whale Tracker MCP** | Whale Alert | Track cryptocurrency whale transactions. | [GitHub](https://github.com/kukapay/whale-tracker-mcp) | [2025-05-07](https://github.com/kukapay/whale-tracker-mcp/commit/96218364c99e6e40c2965744ef93f8ad54236ece) |
| **Crypto Liquidations MCP** | Binance | Real-time liquidation events. | [GitHub](https://github.com/kukapay/crypto-liquidations-mcp) | [2025-05-06](https://github.com/kukapay/crypto-liquidations-mcp/commit/d9a02cda38bdb0f3556fe9a112997f29c82e1900) |
| **Funding Rates MCP** | Major exchanges | Real-time funding rate data. | [GitHub](https://github.com/kukapay/funding-rates-mcp) | [2025-04-21](https://github.com/kukapay/funding-rates-mcp/commit/c508f2e504cce6a7fe05462f2e0c268a2796fb19) |
| **Fear & Greed MCP** | Alternative.me | Crypto Fear & Greed Index data. | [GitHub](https://github.com/kukapay/crypto-feargreed-mcp) | [2025-05-10](https://github.com/kukapay/crypto-feargreed-mcp/commit/b1f22947d81be0e34a502dfed0b866024db46e6a) |
| **BICScan MCP** | BICScan | Blockchain address risk scoring. | [GitHub](https://github.com/ahnlabio/bicscan-mcp) | [2025-03-25](https://github.com/ahnlabio/bicscan-mcp/commit/abf63bb7c439617f492792b3f877b1259d0cb278) |
| **Crypto Sentiment MCP** | Multiple | Cryptocurrency sentiment analysis. | [GitHub](https://github.com/kukapay/crypto-sentiment-mcp) | [2025-03-27](https://github.com/kukapay/crypto-sentiment-mcp/commit/a002ecef5cdd5351e3dd8e03f50c87ef48e3f7dc) |
| **Gas Price MCP** | Blocknative | Real-time gas price predictions across chains. | [GitHub](https://github.com/kukapay/blocknative-mcp) | [2025-04-30](https://github.com/kukapay/blocknative-mcp/commit/c219324996189fc1e5d15048682d2049d809144c) |

## 🌉 Cross-Chain & Bridge MCP Servers

| Name | Description | Link | Last GitHub commit |
| --- | --- | --- | --- |
| **Wormhole MCP** | Automatic token transfers across multiple blockchains via Wormhole SDK. | [GitHub](https://github.com/collinsezedike/wormhole-mcp) | [2025-05-19](https://github.com/collinsezedike/wormhole-mcp/commit/5230b32dc3db651541c04294c06f800c5cfd1c18) |
| **Meson MCP** | Cross-chain transactions for asset transfers. | [GitHub](https://github.com/demcp/demcp-meson-mcp) | [2025-04-28](https://github.com/demcp/demcp-meson-mcp/commit/474554e83030a9167fb5fdc5226b5d54b7f31884) |

## 👛 Wallet & Infrastructure

| Name | Description | Link | Last GitHub commit |
| --- | --- | --- | --- |
| **Trust Wallet Skills + MCP** | Skills for Trust Wallet APIs, CLI tools, and libraries. The wallet skill also covers the CLI MCP server. | [developer.trustwallet.com](https://developer.trustwallet.com/developer/claude-code-skills) · [Source](https://github.com/trustwallet/tw-agent-skills/tree/main/skills) | [2026-06-11](https://github.com/trustwallet/tw-agent-skills/commit/b552e87d00fe6282a28e1946f2f9302f86c5e1f3) |
| **Armor Crypto MCP** | Blockchain interaction, swaps, and strategic planning. | [GitHub](https://github.com/armorwallet/armor-crypto-mcp) | [2025-05-27](https://github.com/armorwallet/armor-crypto-mcp/commit/c026c00b2f3fd40594e31f642d68aa92e742e013) |
| **Thirdweb MCP** | Query real-time blockchain data on EVM chains, access ABIs and source code, execute transactions. | [blog.thirdweb.com](https://blog.thirdweb.com/changelog/thirdweb-mcp-server-v0-1-beta/) | Not verified |
| **Vincent Wallet** | Secure EVM wallet for agent transfers, swaps, and transactions. | [GitHub](https://github.com/HeyVincent-ai/agent-skills/tree/main/wallet) | [2026-03-02](https://github.com/HeyVincent-ai/agent-skills/commit/03fe75a11c7a53edb33aa9cac4cff3ad43bc40d4) |
| **Vincent Polymarket** | Polymarket prediction market trading for agents. | [GitHub](https://github.com/HeyVincent-ai/agent-skills/tree/main/polymarket) | [2026-03-02](https://github.com/HeyVincent-ai/agent-skills/commit/03fe75a11c7a53edb33aa9cac4cff3ad43bc40d4) |
| **AgentFund Skill** | Crowdfunding for AI agents on Base chain — milestone escrow. | [GitHub](https://github.com/RioTheGreat-ai/agentfund-skill) | [2026-02-03](https://github.com/RioTheGreat-ai/agentfund-skill/commit/529bc99175a183f39863ae4a82179f290f5b86de) |
| **CryptoWallet (OpenClaw)** | Multi-chain wallet management — 12 EVM networks. | [LobeHub](https://lobehub.com/skills/openclaw-skills-cryptowallet) | Not verified |
| **Coinbase Agentic Wallet Skills** | Wallet skills for AI agents from Coinbase — install via `npx skills add coinbase/agentic-wallet-skills`. | [GitHub](https://github.com/coinbase/agentic-wallet-skills) | [2026-08-04](https://github.com/coinbase/agentic-wallet-skills/commit/70cb79c85f397fab3636ef07c8c99dc52a7c555f) |
| **Wallet MCP Skill** | Coinbase Wallet Account skill for balances, transfers, swaps, signing, and x402 payments on Base, Ethereum, and other supported chains. Replaces the deprecated `base-mcp` skill. | [Skill](https://github.com/base/skills/tree/master/skills/wallet-mcp) | [2026-10-08](https://github.com/base/skills/commit/ef8bcd52ccc2e79de846cdf8d16b6fc62cf459a4) |
| **Quicknode MCP** | Official Quicknode infrastructure MCP for provisioning endpoints, configuring networks, and monitoring usage. Separate from the QuickNode EVM MCP example above. | [GitHub](https://github.com/quiknode-labs/qn-mcp) | [2026-02-25](https://github.com/quiknode-labs/qn-mcp/commit/5ec23982c7822a2b23712e3842a2af9e936d87ff) |

## 📚 Education

| Name | Description | Link | Last GitHub commit |
| --- | --- | --- | --- |
| **Ethereum-Wingman** | Ethereum development tutor for Scaffold-ETH 2 — fork-mode testing against live protocols. | [LobeHub](https://lobehub.com/skills/openclaw-skills-ethereum-wingman) | Not verified |


## 🗂️ Awesome Lists & Directories

| Name | Description | Link | Last GitHub commit |
| --- | --- | --- | --- |
| **awesome-blockchain-mcps** | Curated list of Blockchain & Crypto MCP servers. | [GitHub](https://github.com/royyannick/awesome-blockchain-mcps) | [2026-03-17](https://github.com/royyannick/awesome-blockchain-mcps/commit/9e6177b6a3543961ea1535daf5552f4b87c8c596) |
| **awesome-crypto-mcp-servers (Hive)** | MCP servers for cryptocurrency, blockchain, and Web3. | [GitHub](https://github.com/hive-intel/awesome-crypto-mcp-servers) | [2026-06-01](https://github.com/hive-intel/awesome-crypto-mcp-servers/commit/fbe5b7602d8cca6fb5b3d52d3cdfd3f217a01916) |
| **awesome-web3-mcp-servers (DeMCP)** | Decentralized MCP network directory. | [GitHub](https://github.com/demcp/awesome-web3-mcp-servers) | [2025-05-22](https://github.com/demcp/awesome-web3-mcp-servers/commit/da1d6edc30556be1c4ae3a575cc08a3349462710) |
| **awesome-blockchain-ai** | Curated list of blockchain projects for AI/ML. | [GitHub](https://github.com/steven2358/awesome-blockchain-ai) | [2026-02-06](https://github.com/steven2358/awesome-blockchain-ai/commit/685d6c782036fd72603e01147216039ca319ba8b) |
| **awesome-x402** | Resources for x402 HTTP 402 Payment Required protocol — blockchain payments, AI agents, API monetization. | [GitHub](https://github.com/xpaysh/awesome-x402) | [2026-07-28](https://github.com/xpaysh/awesome-x402/commit/c45d14ebabb4a696d28758901ee33b2b003d99ba) |

## 🔍 Discovery Resources

> Where to find even more skills as the ecosystem grows.

| Resource | Description | Link |
|----------|-------------|------|
| **agentskills.io** | Central directory of 44k+ agent skills with two-layer security scanning. | [agentskills.io](https://agentskills.io/home) |
| **Skills.sh CLI** | Package manager for the open agent skills ecosystem — `npx skills find ethereum`, `npx skills find defi`. | [skills.sh](https://skills.sh/) |
| **ClawHub** | OpenClaw's marketplace with 27k+ skills. Search "web3" or "defi". **Warning:** 12% of skill packs found to contain malicious code — verify before installing. | [clawhub.com](https://clawhub.com/) |
| **LobeHub Skills Marketplace** | Skills marketplace with crypto/Web3 category. | [lobehub.com/skills](https://lobehub.com/skills) |
| **Termo.ai** | Skill browser — search "ethereum", "crypto", "defi". | [termo.ai](https://termo.ai/) |

---

## Freshness and maintenance

<!-- commits-checked: 2026-10-14 -->

Commit metadata checked on 2026-10-14 (UTC).

`Last GitHub commit` is the UTC committer date of the latest commit on the source repository's default branch. Each date links to that exact commit. For links to a skill file or directory, the date covers only that path and its contents. Repository-root links cover the whole repository, so unrelated changes can make that date recent. The first GitHub link in each row's Link cell defines the source and scope.

`Not verified` means no GitHub source has been verified for that entry. `Unavailable` means GitHub returned 404 for the source repository or no commits for the selected path. `archived` marks a repository that GitHub reports as archived. These states are not evidence that a project is safe or current.

Agents should compare dates with the snapshot date, inspect the linked source for deprecation notices, and check current protocol documentation before using a skill or MCP server. A recent commit does not guarantee current contract addresses, APIs, or dependencies. Hosted services can change independently of their public repositories. This snapshot does not update automatically.

To refresh the snapshot, install Python 3 and the GitHub CLI, authenticate with `gh auth login`, and run from the repository root:

```sh
python3 scripts/refresh-commits.py
```

To compare the table against GitHub without changing the README:

```sh
python3 scripts/refresh-commits.py --check
```

The script uses GitHub commit history rather than repository push timestamps. Use default-branch links for skill files and directories. For website entries, add a verified GitHub source link to the Link cell to include them in the refresh. The script leaves the README unchanged if an API request fails, except for the explicit unavailable states above. Discovery marketplaces have no commit column because a marketplace's own activity says nothing about its listed skills.

## 🤝 Contributing

PRs welcome! If you know of an Ethereum/Web3 AI skill or MCP server not listed here, please open a pull request.

## 📄 License

CC0 1.0 Universal
