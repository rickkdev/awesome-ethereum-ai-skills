# Awesome Ethereum & Web3 AI Skills

A curated list of AI skills, MCP servers, plugins, and agent toolkits for Ethereum and Web3 development. These tools give AI agents (Claude, ChatGPT, Cursor, OpenClaw, etc.) the ability to interact with blockchains, write smart contracts, trade tokens, query on-chain data, and more.

---

## Contents

- [Knowledge & Skill Registries](#knowledge--skill-registries)
- [Protocol-Specific Skills & Plugins](#protocol-specific-skills--plugins)
- [DeFi Protocol Skills](#defi-protocol-skills)
- [Exchange & Trading Skills](#exchange--trading-skills)
- [Smart Contract Security](#smart-contract-security)
- [Oracles & Price Feeds](#oracles--price-feeds)
- [DeFi Data & Analytics](#defi-data--analytics)
- [Agent Frameworks & Toolkits](#agent-frameworks--toolkits)
- [Chain-Specific MCP Servers](#chain-specific-mcp-servers)
- [Ethereum L2 Skills](#ethereum-l2-skills)
- [Trading & DeFi MCP Servers](#trading--defi-mcp-servers)
- [Market Data MCP Servers](#market-data-mcp-servers)
- [Cross-Chain & Bridge Tools](#cross-chain--bridge-tools)
- [Wallet & Infrastructure](#wallet--infrastructure)
- [Standards & Identity](#standards--identity)
- [Frontend & Social](#frontend--social)
- [Dev Tools & Frameworks](#dev-tools--frameworks)
- [Awesome Lists & Directories](#awesome-lists--directories)
- [Discovery Resources](#discovery-resources)

---

## Knowledge & Skill Registries

Everything you need to get started — foundational Ethereum and crypto knowledge packaged as AI skills.

| Name | Description | Link |
|------|-------------|------|
| **ETHSKILLS** | Modular Ethereum knowledge for AI agents — gas, L2s, standards, security, DeFi, auditing, and more. No install required. Built by Austin Griffith / BuidlGuidl / Ethereum Foundation. | [ethskills.com](https://ethskills.com/) |
| **CryptoSkills** | 97+ production-ready AI agent skills across 14 categories and 15 blockchains. Install via `npx cryptoskills install`. | [cryptoskills.dev](https://cryptoskills.dev/) |
| **kukapay/crypto-skills** | Collection of specialized AI agent skills — EVM Swiss Knife, Market Sentiment, Meme Scout, Token Minter, Trading Strategist, Yield Opportunities. Install via `npx skills add kukapay/crypto-skills`. | [GitHub](https://github.com/kukapay/crypto-skills) |
| **crypto-agent-skill** | Real-time crypto market data skill built with the agentskills.io open standard. | [GitHub](https://github.com/JStrait515/crypto-agent-skill) |

## Protocol-Specific Skills & Plugins

| Name | Protocol/Focus | Description | Link |
|------|---------------|-------------|------|
| **Uniswap AI** | Uniswap | Swap integration, pay-with-any-token (x402/MPP), and v4 hook development. Works with Claude Code, MCP, and Skills CLI. | [GitHub](https://github.com/Uniswap/uniswap-ai) |
| **OpenZeppelin Skills** | OpenZeppelin Contracts | Authoritative knowledge of audited smart contract libraries across Solidity, Cairo, Stylus, and Stellar. Covers tokens, access control, governance, and security primitives. | [openzeppelin.com](https://www.openzeppelin.com/news/introducing-openzeppelin-skills) |
| **OpenZeppelin Contracts MCP** | OpenZeppelin Contracts | MCP server that brings security rules, imports, modifiers, and best practices into AI-driven Solidity development. | [mcp.openzeppelin.com](https://mcp.openzeppelin.com/) |
| **UCAI** | Any EVM Contract | Universal Contract AI Interface — generates MCP servers from any ABI. One command to make every function callable by Claude. Supports Uniswap, Aave, ERC20s, NFTs. | [GitHub](https://github.com/nirholas/UCAI) |
| **DeFi Rates MCP** | Aave, Morpho, Compound, etc. | Real-time DeFi lending rates across 13+ protocols. | [GitHub](https://github.com/qingfeng/defi-rates-mcp) |
| **Chainlink Feeds MCP** | Chainlink | Real-time access to Chainlink's decentralized price feeds on Ethereum, Base, and more. | [mcplane.com](https://www.mcplane.com/mcp_servers/chainlink-feeds) |
| **Alchemy Skills** | Alchemy (Multi-chain) | Agent Skills for all Alchemy products — EVM JSON-RPC, Token API, NFT API, Prices API, Portfolio API, Webhooks. Supports API key, x402, and MPP access. Install via `npx skills add alchemyplatform/skills -g --yes`. | [GitHub](https://github.com/alchemyplatform/skills) |
| **Arbitrum dApp Skill** | Arbitrum | Claude Code skill for scaffolding complete Arbitrum dApps — Stylus Rust + Solidity contracts, React frontends, local devnode, deployment to Sepolia/One. | [GitHub](https://github.com/hummusonrails/arbitrum-dapp-skill) |
| **Hyperlane MCP** | Hyperlane | Interoperability tooling for interchain AI agents. | [hyperlane.xyz](https://www.hyperlane.xyz/post/introducing-hyperlane-mcp-tooling-for-interchain-agents) |
| **Brian API** | Natural Language → Web3 | Converts natural language to Web3 transactions. | [brian.so](https://www.brian.so/) |
| **ENS Skill** | Ethereum Name Service | ENS name resolution, registration, and management. | [cryptoskills.dev](https://cryptoskills.dev/) |
| **Farcaster Skill** | Farcaster | Onchain social protocol — Neynar API, Frames v2, channels, casts. | [cryptoskills.dev](https://cryptoskills.dev/) |

## DeFi Protocol Skills

Production-ready skills for specific DeFi protocols — available via [CryptoSkills](https://cryptoskills.dev/) or standalone.

| Name | Protocol | Description | Link |
|------|----------|-------------|------|
| **Aave V3 Skill** | Aave | Supply, borrow, repay, withdraw, flash loans, E-Mode, health factor monitoring. IPool interface in Solidity + viem-based TypeScript. | [cryptoskills.dev](https://cryptoskills.dev/) |
| **Compound V3 Skill** | Compound | Comet single-asset borrowing, governance, and COMP distribution. | [cryptoskills.dev](https://cryptoskills.dev/) |
| **Curve Finance Skill** | Curve | StableSwap AMM, crvUSD stablecoin, gauge voting. | [cryptoskills.dev](https://cryptoskills.dev/) |
| **Lido Skill** | Lido | Liquid staking — stETH/wstETH mechanics, staking, and wrapping. | [cryptoskills.dev](https://cryptoskills.dev/) |
| **EigenLayer Skill** | EigenLayer | ETH restaking to secure AVSs (Actively Validated Services). | [cryptoskills.dev](https://cryptoskills.dev/) |
| **Maker/Sky Skill** | MakerDAO / Sky | DAI minting via vaults, DSR, Liquidation 2.0. | [cryptoskills.dev](https://cryptoskills.dev/) |
| **Morpho Blue Skill** | Morpho | Permissionless lending markets with isolated risk. | [cryptoskills.dev](https://cryptoskills.dev/) |
| **Pendle Skill** | Pendle | Yield tokenization — PT/YT trading and strategies. | [cryptoskills.dev](https://cryptoskills.dev/) |
| **GMX V2 Skill** | GMX | Perpetuals (50x leverage) and spot DEX on Arbitrum/Avalanche. | [cryptoskills.dev](https://cryptoskills.dev/) |
| **Vertex Skill** | Vertex | Cross-chain spot, perpetuals, and money markets. | [cryptoskills.dev](https://cryptoskills.dev/) |
| **Safe Skill** | Safe (Gnosis Safe) | Multisig SDK across 20+ chains — setup, signing, execution. | [cryptoskills.dev](https://cryptoskills.dev/) |
| **Polymarket Skill** | Polymarket | CLOB integration, HMAC signing, CTF operations for prediction markets. | [cryptoskills.dev](https://cryptoskills.dev/) |
| **Metengine Skill** | Metengine | Smart money analytics for Polymarket and Hyperliquid. | [cryptoskills.dev](https://cryptoskills.dev/) |

## Exchange & Trading Skills

| Name | Platform | Description | Link |
|------|----------|-------------|------|
| **Binance AI Agent Skills** | Binance | 11 modular skills for spot trading, derivatives, margin, market intelligence, token auditing, asset management, and Binance Alpha data. | [binance.com](https://www.binance.com/en/support/announcement/detail/bafb9dda6cbb47d5882a4090c31d4c64) |
| **Bybit AI Skills** | Bybit | 253 API endpoints — market intelligence, spot trading, derivatives, earn products, account management. Works with ChatGPT, Claude, OpenClaw, Cursor. | [chainwire.org](https://chainwire.org/2026/03/13/bybit-launches-ai-skills-powering-ai-agents-for-crypto-trading-with-zero-setup-253-api-endpoints-and-growing/) |
| **KuCoin Skills Hub** | KuCoin | Open skills marketplace for AI-driven crypto access — market data, analytics, trading signals. Expanding to wallet ops, staking, lending, and yield. | [kucoin.com](https://www.kucoin.com/announcement/en-kucoin-skills-hub-is-now-live-connecting-ai-agents-to-the-kucoin-exchange) |
| **Bitget Wallet Skill** | Bitget | AI agent suite for onchain market data, trading infrastructure, and blockchain data via natural language. | [bitcoinethereumnews.com](https://bitcoinethereumnews.com/tech/bitget-wallet-expands-into-ai-agent-capabilities-with-skill-beta/) |
| **Hyperliquid Skill** | Hyperliquid | Perpetual futures (50x leverage), WebSocket streaming, order management. | [cryptoskills.dev](https://cryptoskills.dev/) |

## Smart Contract Security

| Name | Focus | Description | Link |
|------|-------|-------------|------|
| **ETHSKILLS Audit** | Solidity | 500+ item contract audit system with specialist agents. | [ethskills.com](https://ethskills.com/) |
| **OpenZeppelin Skills** | Solidity, Cairo, Stylus | Security-critical patterns: ReentrancyGuard, Pausable, AccessControl, and more. | [openzeppelin.com](https://www.openzeppelin.com/news/introducing-openzeppelin-skills) |
| **QuillShield** | Solidity | AI-powered vulnerability detection that learns from past exploits, reduces false positives. | [quillaudits.com](https://www.quillaudits.com/) |
| **Slither** | Solidity | Python-based static analysis with 92+ vulnerability detectors. Trail of Bits. | [GitHub](https://github.com/crytic/slither) |
| **Echidna** | Solidity | Property-based fuzzing for Ethereum smart contracts. Trail of Bits. | [GitHub](https://github.com/crytic/echidna) |
| **EVM MCP Tools** | EVM | Blockchain analysis toolkit for Claude — audit smart contracts, analyze wallets, track profitability, fetch on-chain data via MCP. | [GitHub](https://github.com/0xGval/evm-mcp-tools) |
| **Certora Skill** | Solidity | Formal verification with CVL (Certora Verification Language). | [cryptoskills.dev](https://cryptoskills.dev/) |
| **Halmos Skill** | Solidity | Symbolic testing for Foundry-based smart contracts. | [cryptoskills.dev](https://cryptoskills.dev/) |
| **Mythril Skill** | Solidity | Symbolic execution engine for vulnerability detection in EVM bytecode. | [cryptoskills.dev](https://cryptoskills.dev/) |
| **Semgrep-Solidity Skill** | Solidity | Custom pattern matching rules for Solidity static analysis. | [cryptoskills.dev](https://cryptoskills.dev/) |
| **Solidity-Auditor Skill** | Solidity | Real-time code audit skill for live Solidity development. | [cryptoskills.dev](https://cryptoskills.dev/) |
| **Solidity-Security Skill** | Solidity | Security patterns and vulnerability prevention reference. | [cryptoskills.dev](https://cryptoskills.dev/) |
| **Vulnhunter Skill** | Solidity | Vulnerability variant analysis across smart contracts. | [cryptoskills.dev](https://cryptoskills.dev/) |
| **Code-Recon Skill** | Solidity | Architectural auditing methodology for code review. | [cryptoskills.dev](https://cryptoskills.dev/) |
| **SecSkills Web3** | Web3 Security | Security-first Web3 development for Ethereum and EVM chains. | [LobeHub](https://lobehub.com/skills/trilwu-secskills-web3-blockchain) |

## Oracles & Price Feeds

| Name | Protocol | Description | Link |
|------|----------|-------------|------|
| **Chainlink Skill** | Chainlink | Price feeds, VRF v2.5, Automation (Keepers), and CCIP cross-chain messaging across Ethereum, Arbitrum, Base. | [cryptoskills.dev](https://cryptoskills.dev/) |
| **Pyth-EVM Skill** | Pyth (EVM) | Pull oracle for EVM chains with Hermes API. | [cryptoskills.dev](https://cryptoskills.dev/) |
| **RedStone Skill** | RedStone | Modular oracle with pull/push delivery models. | [cryptoskills.dev](https://cryptoskills.dev/) |

## DeFi Data & Analytics

| Name | Focus | Description | Link |
|------|-------|-------------|------|
| **Dune Analytics MCP** | On-chain data | Connects AI agents to Dune's data warehouse across 100+ blockchains. Query stablecoin flows, DEX volumes via natural language. | [GitHub](https://github.com/kukapay/dune-analytics-mcp) |
| **Dune CLI + Skills** | On-chain data | CLI and Skills framework for autonomous on-chain queries across 130+ chains. | [blockchain.news](https://blockchain.news/news/dune-analytics-agent-native-cli-skills-launch) |
| **Zerion MCP + Skills** | Portfolio & on-chain data | Connects Claude to on-chain data for portfolio analysis, wallet tracking, and DeFi research. | [zerion.io](https://zerion.io/blog/zerion-for-api-ai-agents-mcp-skills/) |
| **The Graph MCP** | Indexed blockchain data | Query indexed blockchain data from The Graph's subgraphs. | [GitHub](https://github.com/kukapay/thegraph-mcp) |
| **DeFi Llama MCP** | DeFi analytics | API wrapper around the DeFi Llama ecosystem for TVL, yield, and protocol data. | [GitHub](https://github.com/demcp/defillama-mcp) |
| **Hive Intelligence** | Multi-chain | MCP server connecting AI agents to 60+ blockchains with real-time crypto data. Works with Claude, ChatGPT, LangChain. | [hiveintelligence.xyz](https://hiveintelligence.xyz/) |
| **Codex MCP** | Multi-chain | Enriched blockchain data from Codex. | [GitHub](https://github.com/Codex-Data/codex-mcp) |
| **Tenderly Skill** | DevOps | Simulation, debugging, transaction tracing, and monitoring for EVM chains. | [cryptoskills.dev](https://cryptoskills.dev/) |

## Agent Frameworks & Toolkits

| Name | Description | Link |
|------|-------------|------|
| **Coinbase AgentKit** | Model-agnostic toolkit giving AI agents crypto wallets and on-chain interactions. Plug-and-play skills: authenticate, fund, send, trade, earn. | [GitHub](https://github.com/coinbase/agentkit) |
| **GOAT (Great Onchain Agent Toolkit)** | Universal adapter between AI agents and any blockchain app. 200+ plugins across 30+ chains. Works with Langchain, Vercel AI SDK, ElizaOS, MCP. | [GitHub](https://github.com/goat-sdk/goat) |
| **ElizaOS** | AI agent framework built for Web3 from day one. Production-proven blockchain integrations, originally launched as ai16z. | [GitHub](https://github.com/elizaOS/eliza) |
| **OpenClaw** | Open-source local-first AI agent framework. 2M+ users, integrates with Claude, GPT, and Web3 skills for wallet management, token swaps, and stablecoin payments. | [openclaw.com](https://openclaw.com) |
| **x402** | HTTP 402 payment protocol enabling machine-to-machine commerce and agent payments. | [cryptoskills.dev](https://cryptoskills.dev/) |
| **eth-agent** | TypeScript library giving AI agents a simple, safe interface to send stablecoins (USDC/USDT/DAI) and ETH across chains. | [LobeHub](https://lobehub.com/skills/lambdaclass-eth-agent-eth-agent) |

## Chain-Specific MCP Servers

| Name | Chain | Description | Link |
|------|-------|-------------|------|
| **Base MCP** | Base | Official — "provides tools to do anything on Base." | [GitHub](https://github.com/base/base-mcp) |
| **Etherscan MCP** | Ethereum | Ethereum blockchain data tools via Etherscan API. | [GitHub](https://github.com/crazyrabbitLTC/mcp-etherscan-server) |
| **eth-mcp** | Ethereum | Direct Ethereum blockchain interaction. | [GitHub](https://github.com/0xKoda/eth-mcp) |
| **QuickNode EVM MCP** | Multi-EVM | Multichain RPC server (Ethereum, Arbitrum, Base, BSC) using Viem. | [quicknode.com](https://www.quicknode.com/guides/ai/evm-mcp-server) |
| **evm-mcp-server** | Multi-EVM | Blockchain services across multiple EVM-compatible networks. | [GitHub](https://github.com/mcpdotdirect/evm-mcp-server) |
| **Strangelove web3-mcp** | Multi-chain | "1 MCP to rule all them chains" — includes Ethereum and EVM chains. | [GitHub](https://github.com/strangelove-ventures/web3-mcp) |
| **BSC MCP** | Binance Smart Chain | Token transfers and smart contract interaction on BSC. | [GitHub](https://github.com/TermiX-official/bsc-mcp) |
| **Polygon MCP** | Polygon PoS | On-chain tools for Claude AI on Polygon. | [GitHub](https://github.com/Dablclub/polygon-mcp) |
| **StarkNet MCP** | StarkNet | Query blockchain data, manage wallets, interact with smart contracts. | [GitHub](https://github.com/mcpdotdirect/starknet-mcp-server) |
| **Alchemy SDK MCP** | Multi-chain | Integration with Alchemy SDK for blockchain and NFT operations. | [GitHub](https://github.com/itsanishjain/alchemy-sdk-mcp) |
| **Linea MCP** | Linea | On-chain tools for AI applications on Linea. | [GitHub](https://github.com/qvkare/linea-mcp) |
| **Nodit MCP** | Multi-chain | Structured, context-ready blockchain data. | [GitHub](https://github.com/noditlabs/nodit-mcp-server) |
| **Bankless Onchain MCP** | Multi-chain | Blockchain data interaction through the Bankless API. | [GitHub](https://github.com/Bankless/onchain-mcp) |
| **Web3 Agent MCP** | Multi-chain | Ethereum, Polygon, Arbitrum, Optimism, Base, Avalanche — DeFi protocol interactions (Aave, Balancer, Convex, Curve, GMX, Morpho). | [LobeHub](https://lobehub.com/mcp/whatl3y-web3-agent) |

## Ethereum L2 Skills

| Name | Chain | Description | Link |
|------|-------|-------------|------|
| **Arbitrum Skill** | Arbitrum | Nitro L2, Orbit chains, cross-chain messaging. | [cryptoskills.dev](https://cryptoskills.dev/) |
| **Arbitrum Stylus Skill** | Arbitrum Stylus | Rust/C++ smart contracts compiled to WASM on Arbitrum. | [cryptoskills.dev](https://cryptoskills.dev/) |
| **Base Skill** | Base | Coinbase L2 on OP Stack with OnchainKit. | [cryptoskills.dev](https://cryptoskills.dev/) |
| **Optimism Skill** | Optimism | OP Stack, SuperchainERC20, Superchain interop. | [cryptoskills.dev](https://cryptoskills.dev/) |
| **Polygon Skill** | Polygon | PoS chain, zkEVM, AggLayer. | [cryptoskills.dev](https://cryptoskills.dev/) |
| **StarkNet Skill** | StarkNet | Cairo smart contracts, native account abstraction. | [cryptoskills.dev](https://cryptoskills.dev/) |
| **Linea Skill** | Linea | Consensys zkEVM L2. | [cryptoskills.dev](https://cryptoskills.dev/) |
| **MegaETH Skill** | MegaETH | Real-time Ethereum L2 with instant receipts. | [cryptoskills.dev](https://cryptoskills.dev/) |

## Trading & DeFi MCP Servers

| Name | Focus | Description | Link |
|------|-------|-------------|------|
| **Binance MCP** | Binance | Interact with Binance API. | [GitHub](https://github.com/TermiX-official/binance-mcp) |
| **Uniswap Trader MCP** | Uniswap | Automate token swaps on Uniswap DEX. | [GitHub](https://github.com/kukapay/uniswap-trader-mcp) |
| **Uniswap PoolSpy MCP** | Uniswap | Track newly created liquidity pools on Uniswap (9 networks). | [GitHub](https://github.com/kukapay/uniswap-poolspy-mcp) |
| **PancakeSwap PoolSpy MCP** | PancakeSwap | Track newly created liquidity pools. | [GitHub](https://github.com/kukapay/pancakeswap-poolspy-mcp) |
| **Hyperliquid MCP** | Hyperliquid | Integrates the Hyperliquid SDK. | [GitHub](https://github.com/mektigboy/server-hyperliquid) |
| **DeFi Yields MCP** | Multi-protocol | Explore DeFi yield opportunities across protocols. | [GitHub](https://github.com/kukapay/defi-yields-mcp) |
| **Bridge Rates MCP** | Cross-chain | Real-time cross-chain bridge rates. | [GitHub](https://github.com/kukapay/bridge-rates-mcp) |
| **Token Revoke MCP** | Multi-chain | Check and revoke ERC-20 token allowances. | [GitHub](https://github.com/kukapay/token-revoke-mcp) |
| **Token Minter MCP** | 21 chains | Mint ERC-20 tokens across 21 blockchains. | [GitHub](https://github.com/kukapay/token-minter-mcp) |
| **Free USDC Transfer MCP** | Base | Free USDC transfers on Base. | [GitHub](https://github.com/magnetai/mcp-free-usdc-transfer) |
| **Bybit MCP** | Bybit | Read-only access to Bybit exchange API. | [GitHub](https://github.com/sammcj/bybit-mcp) |
| **Freqtrade MCP** | Freqtrade | Integration with Freqtrade crypto trading bot. | [GitHub](https://github.com/kukapay/freqtrade-mcp) |

## Market Data MCP Servers

| Name | Source | Description | Link |
|------|--------|-------------|------|
| **CoinGecko MCP** | CoinGecko Pro | CoinGecko Pro API integration. | [GitHub](https://github.com/crazyrabbitLTC/mcp-coingecko-server) |
| **CoinMarketCap MCP** | CoinMarketCap | Real-time prices, market cap, and volume. | [GitHub](https://github.com/anjor/coinmarket-mcp-server) |
| **CoinStats MCP** | CoinStats | Market data, portfolio tracking, and news. | [GitHub](https://github.com/CoinStatsHQ/coinstats-mcp) |
| **CCXT MCP** | Major exchanges | Real-time and historical market data via CCXT. | [GitHub](https://github.com/Nayshins/mcp-server-ccxt) |
| **DexScreener MCP** | DexScreener | DEX pair data, token info, and market statistics. | [GitHub](https://github.com/openSVM/dexscreener-mcp-server) |
| **Whale Tracker MCP** | Whale Alert | Track cryptocurrency whale transactions. | [GitHub](https://github.com/kukapay/whale-tracker-mcp) |
| **Crypto Liquidations MCP** | Binance | Real-time liquidation events. | [GitHub](https://github.com/kukapay/crypto-liquidations-mcp) |
| **Funding Rates MCP** | Major exchanges | Real-time funding rate data. | [GitHub](https://github.com/kukapay/funding-rates-mcp) |
| **Fear & Greed MCP** | Alternative.me | Crypto Fear & Greed Index data. | [GitHub](https://github.com/kukapay/crypto-feargreed-mcp) |
| **BICScan MCP** | BICScan | Blockchain address risk scoring. | [GitHub](https://github.com/ahnlabio/bicscan-mcp) |
| **Crypto Sentiment MCP** | Multiple | Cryptocurrency sentiment analysis. | [GitHub](https://github.com/kukapay/crypto-sentiment-mcp) |
| **Gas Price MCP** | Blocknative | Real-time gas price predictions across chains. | [GitHub](https://github.com/kukapay/blocknative-mcp) |

## Cross-Chain & Bridge Tools

| Name | Description | Link |
|------|-------------|------|
| **Wormhole MCP** | Automatic token transfers across multiple blockchains via Wormhole SDK. | [GitHub](https://github.com/collinsezedike/wormhole-mcp) |
| **Wormhole Skill** | NTT framework, VAAs, cross-chain reads. | [cryptoskills.dev](https://cryptoskills.dev/) |
| **Hyperlane MCP** | Interoperability tooling for interchain AI agents. | [hyperlane.xyz](https://www.hyperlane.xyz/post/introducing-hyperlane-mcp-tooling-for-interchain-agents) |
| **Hyperlane Skill** | Permissionless Mailbox messaging, Warp Routes. | [cryptoskills.dev](https://cryptoskills.dev/) |
| **LayerZero V2 Skill** | V2 OApp framework, OFT tokens for omnichain messaging. | [cryptoskills.dev](https://cryptoskills.dev/) |
| **Axelar Skill** | GMP messaging, ITS multichain tokens. | [cryptoskills.dev](https://cryptoskills.dev/) |
| **deBridge Skill** | Cross-chain bridges and message passing (EVM focus). | [cryptoskills.dev](https://cryptoskills.dev/) |
| **Meson MCP** | Cross-chain transactions for asset transfers. | [GitHub](https://github.com/demcp/demcp-meson-mcp) |
| **Bridge Rates MCP** | Real-time cross-chain bridge rate comparison. | [GitHub](https://github.com/kukapay/bridge-rates-mcp) |

## Wallet & Infrastructure

| Name | Description | Link |
|------|-------------|------|
| **Trust Wallet Skills + MCP** | Claude Code skills marketplace + MCP server for Trust Wallet APIs, chains, and wallet functions. | [developer.trustwallet.com](https://developer.trustwallet.com/developer/claude-code-skills) |
| **Coinbase AgentKit** | Agentic wallets on Base with TEE-isolated private keys. Model-agnostic (Claude, GPT, OpenClaw). | [GitHub](https://github.com/coinbase/agentkit) |
| **Armor Crypto MCP** | Blockchain interaction, swaps, and strategic planning. | [GitHub](https://github.com/armorwallet/armor-crypto-mcp) |
| **Thirdweb MCP** | Query real-time blockchain data on EVM chains, access ABIs and source code, execute transactions. | [blog.thirdweb.com](https://blog.thirdweb.com/changelog/thirdweb-mcp-server-v0-1-beta/) |
| **Vincent Wallet** | Secure EVM wallet for agent transfers, swaps, and transactions. | [GitHub](https://github.com/HeyVincent-ai/agent-skills/tree/main/wallet) |
| **Vincent Polymarket** | Polymarket prediction market trading for agents. | [GitHub](https://github.com/HeyVincent-ai/agent-skills/tree/main/polymarket) |
| **AgentFund Skill** | Crowdfunding for AI agents on Base chain — milestone escrow. | [GitHub](https://github.com/RioBot-Grind/agentfund-skill) |
| **CryptoWallet (OpenClaw)** | Multi-chain wallet management — 12 EVM networks. | [LobeHub](https://lobehub.com/skills/openclaw-skills-cryptowallet) |
| **Privy Skill** | Embedded wallet with social/email/passkey auth for dApps. | [cryptoskills.dev](https://cryptoskills.dev/) |

## Standards & Identity

| Name | Description | Link |
|------|-------------|------|
| **Account Abstraction Skill** | ERC-4337 v0.7, EIP-7702, EntryPoint lifecycle, bundlers, paymasters. | [cryptoskills.dev](https://cryptoskills.dev/) |
| **EIP-Reference Skill** | ERC-20, ERC-721, ERC-1155, ERC-4626, EIP-712, EIP-4337, EIP-7702 reference. | [cryptoskills.dev](https://cryptoskills.dev/) |
| **ERC-8004** | Onchain agent identity standard — deployed on 20+ chains. Co-led by Ethereum Foundation, MetaMask, and Google. | [ethereum.org](https://ethereum.org/ai-agents/) |
| **Eth-Concepts Skill** | Core Ethereum — gas mechanics, transaction types, storage layout, ABI encoding, EVM execution. | [cryptoskills.dev](https://cryptoskills.dev/) |
| **Contract-Addresses Skill** | Verified contract addresses across EVM chains. | [cryptoskills.dev](https://cryptoskills.dev/) |
| **EVM-NFTs Skill** | ERC-721/1155 patterns, Seaport marketplace integration. | [cryptoskills.dev](https://cryptoskills.dev/) |

## Frontend & Social

| Name | Description | Link |
|------|-------------|------|
| **Wagmi Skill** | React hooks for Ethereum — useReadContract, useWriteContract, wallet connection. | [cryptoskills.dev](https://cryptoskills.dev/) |
| **Frontend-UX Skill** | dApp patterns — wallet connection flows, transaction UX, error handling. | [cryptoskills.dev](https://cryptoskills.dev/) |
| **Ethereum-Wingman** | Ethereum development tutor for Scaffold-ETH 2 — fork-mode testing against live protocols. | [LobeHub](https://lobehub.com/skills/openclaw-skills-ethereum-wingman) |
| **Web3 Community Skill** | Web3 community management and engagement patterns. | [LobeHub](https://lobehub.com/skills/omer-metin-skills-for-antigravity-web3-community) |

## Dev Tools & Frameworks

| Name | Description | Link |
|------|-------------|------|
| **Foundry MCP Server** | Experimental MCP server for Foundry — built for Solidity devs. | [GitHub](https://github.com/PraneshASP/foundry-mcp-server) |
| **Foundry Skill** | Full Forge/Cast/Anvil/Chisel toolkit — build, test, deploy, and debug Solidity. | [cryptoskills.dev](https://cryptoskills.dev/) |
| **Hardhat Skill** | Solidity development framework with plugins, testing, and deployment. | [cryptoskills.dev](https://cryptoskills.dev/) |
| **Scaffold-ETH-2 Skill** | Full-stack dApp framework — Hardhat + Next.js + wagmi scaffolding. | [cryptoskills.dev](https://cryptoskills.dev/) |
| **Viem Skill** | TypeScript Ethereum interface — modern, type-safe alternative to ethers.js. | [cryptoskills.dev](https://cryptoskills.dev/) |
| **Ethers.js Skill** | v6 TypeScript library for Ethereum interactions. | [cryptoskills.dev](https://cryptoskills.dev/) |
| **EVM Testing Skill** | Unit, fuzz, invariant, and fork testing patterns for smart contracts. | [cryptoskills.dev](https://cryptoskills.dev/) |
| **Lyra Tool Discovery** | AI-powered automation that discovers MCP servers for you. Point it at GitHub/npm, get ready-to-ship plugin configs. | [GitHub](https://github.com/nirholas/lyra-tool-discovery) |
| **Skill-to-MCP** | Convert AI Skills (Claude Skills format) to MCP server resources. | [GitHub](https://github.com/biocontext-ai/skill-to-mcp) |
| **SpoonOS Web3 Skills** | 57 Python scripts across 19 skills for Web3 integrations (DeFi, NFT, DAO, Security). | [GitHub](https://github.com/XSpoonAi/spoon-awesome-skill) |
| **Web3 Research MCP** | Deep research for crypto — local analysis and research automation. | [GitHub](https://github.com/aaronjmars/web3-research-mcp) |
| **Crypto-Skill-Creator** | Framework and guide for contributing new CryptoSkills to the registry. | [cryptoskills.dev](https://cryptoskills.dev/) |
| **Web3 Testing Skill** | Smart contract testing workflow with Hardhat + Foundry — unit, integration, fuzzing, gas profiling, fork testing. | [LobeHub](https://lobehub.com/skills/agent-skills-hub-agent-skills-hub-web3-testing) |

## Awesome Lists & Directories

| Name | Description | Link |
|------|-------------|------|
| **awesome-blockchain-mcps** | Curated list of Blockchain & Crypto MCP servers. | [GitHub](https://github.com/royyannick/awesome-blockchain-mcps) |
| **awesome-crypto-mcp-servers (Hive)** | MCP servers for cryptocurrency, blockchain, and Web3. | [GitHub](https://github.com/hive-intel/awesome-crypto-mcp-servers) |
| **awesome-web3-mcp-servers (DeMCP)** | Decentralized MCP network directory. | [GitHub](https://github.com/demcp/awesome-web3-mcp-servers) |
| **awesome-blockchain-ai** | Curated list of blockchain projects for AI/ML. | [GitHub](https://github.com/steven2358/awesome-blockchain-ai) |
| **awesome-x402** | Resources for x402 HTTP 402 Payment Required protocol — blockchain payments, AI agents, API monetization. | [GitHub](https://github.com/xpaysh/awesome-x402) |
| **awesome-agent-skills (heilcheng)** | 500+ curated AI agent skills across all domains including Web3. | [GitHub](https://github.com/heilcheng/awesome-agent-skills) |
| **awesome-agent-skills (VoltAgent)** | 549+ skills from official dev teams (includes Binance Web3 skills). | [GitHub](https://github.com/VoltAgent/awesome-agent-skills) |
| **awesome-openclaw-skills (VoltAgent)** | 5,400+ OpenClaw skills filtered and categorized. | [GitHub](https://github.com/VoltAgent/awesome-openclaw-skills) |
| **awesome-agent-skills (skillmatic)** | The definitive resource for Agent Skills — modular capabilities for AI agents. | [GitHub](https://github.com/skillmatic-ai/awesome-agent-skills) |
| **awesome-layerzero** | Everything about LayerZero in one resource. | [GitHub](https://github.com/LayerZero-Labs/awesome-layerzero) |

## Discovery Resources

Where to find even more skills as the ecosystem grows.

| Resource | Description | Link |
|----------|-------------|------|
| **agentskills.io** | Central directory of 44k+ agent skills with two-layer security scanning. | [agentskills.io](https://agentskills.io/home) |
| **Skills.sh CLI** | Package manager for the open agent skills ecosystem — `npx skills find ethereum`, `npx skills find defi`. | [skills.sh](https://skills.sh/) |
| **ClawHub** | OpenClaw's marketplace with 27k+ skills. Search "web3" or "defi". **Warning:** 12% of skill packs found to contain malicious code — verify before installing. | [clawhub.com](https://clawhub.com/) |
| **LobeHub Skills Marketplace** | Skills marketplace with crypto/Web3 category. | [lobehub.com/skills](https://lobehub.com/skills) |
| **Termo.ai** | Skill browser — search "ethereum", "crypto", "defi". | [termo.ai](https://termo.ai/) |
| **roadmap.sh/blockchain** | Structured learning roadmap for blockchain — Solidity/Rust, frameworks, L2s, security, oracles, cross-chain. | [roadmap.sh](https://roadmap.sh/blockchain) |
| **GitHub Search** | Search `"agent-skills" + protocol_name` or `"mcp-server" + protocol_name` for protocol-specific tools. | [github.com](https://github.com/search) |

---

## Contributing

PRs welcome! If you know of an Ethereum/Web3 AI skill, MCP server, or agent toolkit not listed here, please open a pull request.

## License

CC0 1.0 Universal
