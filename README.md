# Awesome Ethereum & Web3 AI Skills

A curated list of AI skills, MCP servers, plugins, and agent toolkits for Ethereum and Web3 development. These tools give AI agents (Claude, ChatGPT, Cursor, OpenClaw, etc.) the ability to interact with blockchains, write smart contracts, trade tokens, query on-chain data, and more.

---

## Contents

- [Knowledge & Skill Registries](#knowledge--skill-registries)
- [Protocol-Specific Skills & Plugins](#protocol-specific-skills--plugins)
- [Exchange & Trading Skills](#exchange--trading-skills)
- [Smart Contract Security](#smart-contract-security)
- [DeFi Data & Analytics](#defi-data--analytics)
- [Agent Frameworks & Toolkits](#agent-frameworks--toolkits)
- [Chain-Specific MCP Servers](#chain-specific-mcp-servers)
- [Trading & DeFi MCP Servers](#trading--defi-mcp-servers)
- [Market Data MCP Servers](#market-data-mcp-servers)
- [Cross-Chain & Bridge Tools](#cross-chain--bridge-tools)
- [Wallet & Infrastructure](#wallet--infrastructure)
- [Dev Tools](#dev-tools)
- [Awesome Lists](#awesome-lists)

---

## Knowledge & Skill Registries

Everything you need to get started — foundational Ethereum and crypto knowledge packaged as AI skills.

| Name | Description | Link |
|------|-------------|------|
| **ETHSKILLS** | Modular Ethereum knowledge for AI agents — gas, L2s, standards, security, DeFi, auditing, and more. No install required. | [ethskills.com](https://ethskills.com/) |
| **CryptoSkills** | 97+ production-ready AI agent skills across 14 categories. Install via `npx cryptoskills install`. | [cryptoskills.dev](https://cryptoskills.dev/) |

## Protocol-Specific Skills & Plugins

| Name | Protocol/Focus | Description | Link |
|------|---------------|-------------|------|
| **Uniswap AI** | Uniswap | Swap integration, pay-with-any-token (x402/MPP), and v4 hook development. Works with Claude Code, MCP, and Skills CLI. | [GitHub](https://github.com/Uniswap/uniswap-ai) |
| **OpenZeppelin Skills** | OpenZeppelin Contracts | Authoritative knowledge of audited smart contract libraries across Solidity, Cairo, Stylus, and Stellar. Covers tokens, access control, governance, and security primitives. | [openzeppelin.com](https://www.openzeppelin.com/news/introducing-openzeppelin-skills) |
| **OpenZeppelin Contracts MCP** | OpenZeppelin Contracts | MCP server that brings security rules, imports, modifiers, and best practices into AI-driven Solidity development. | [mcp.openzeppelin.com](https://mcp.openzeppelin.com/) |
| **UCAI** | Any EVM Contract | Universal Contract AI Interface — generates MCP servers from any ABI. One command to make every function callable by Claude. Supports Uniswap, Aave, ERC20s, NFTs. | [GitHub](https://github.com/nirholas/UCAI) |
| **DeFi Rates MCP** | Aave, Morpho, Compound, etc. | Real-time DeFi lending rates across 13+ protocols. | [GitHub](https://github.com/qingfeng/defi-rates-mcp) |
| **Chainlink Feeds MCP** | Chainlink | Real-time access to Chainlink's decentralized price feeds on Ethereum, Base, and more. | [mcplane.com](https://www.mcplane.com/mcp_servers/chainlink-feeds) |
| **Alchemy Skills** | Alchemy (Multi-chain) | Agent Skills for all Alchemy products — EVM JSON-RPC, Token API, NFT API, Prices API, Portfolio API, Webhooks, Solana. Supports API key, x402, and MPP access. Install via `npx skills add alchemyplatform/skills -g --yes`. | [GitHub](https://github.com/alchemyplatform/skills) |
| **Arbitrum dApp Skill** | Arbitrum | Claude Code skill for scaffolding complete Arbitrum dApps — Stylus Rust + Solidity contracts, React frontends, local devnode, deployment to Sepolia/One. | [GitHub](https://github.com/hummusonrails/arbitrum-dapp-skill) |
| **Hyperlane MCP** | Hyperlane | Interoperability tooling for interchain AI agents. | [hyperlane.xyz](https://www.hyperlane.xyz/post/introducing-hyperlane-mcp-tooling-for-interchain-agents) |

## Exchange & Trading Skills

| Name | Platform | Description | Link |
|------|----------|-------------|------|
| **Binance AI Agent Skills** | Binance | 11 modular skills for spot trading, derivatives, margin, market intelligence, token auditing, asset management, and Binance Alpha data. | [binance.com](https://www.binance.com/en/support/announcement/detail/bafb9dda6cbb47d5882a4090c31d4c64) |
| **Bybit AI Skills** | Bybit | 253 API endpoints — market intelligence, spot trading, derivatives, earn products, account management. Works with ChatGPT, Claude, OpenClaw, Cursor. | [chainwire.org](https://chainwire.org/2026/03/13/bybit-launches-ai-skills-powering-ai-agents-for-crypto-trading-with-zero-setup-253-api-endpoints-and-growing/) |
| **KuCoin Skills Hub** | KuCoin | Open skills marketplace for AI-driven crypto access — market data, analytics, trading signals. Expanding to wallet ops, staking, lending, and yield. | [kucoin.com](https://www.kucoin.com/announcement/en-kucoin-skills-hub-is-now-live-connecting-ai-agents-to-the-kucoin-exchange) |

## Smart Contract Security

| Name | Focus | Description | Link |
|------|-------|-------------|------|
| **ETHSKILLS Audit** | Solidity | 500+ item contract audit system with specialist agents. | [ethskills.com](https://ethskills.com/) |
| **OpenZeppelin Skills** | Solidity, Cairo, Stylus | Security-critical patterns: ReentrancyGuard, Pausable, AccessControl, and more. | [openzeppelin.com](https://www.openzeppelin.com/news/introducing-openzeppelin-skills) |
| **QuillShield** | Solidity | AI-powered vulnerability detection that learns from past exploits, reduces false positives. | [quillaudits.com](https://www.quillaudits.com/) |
| **Slither** | Solidity | Python-based static analysis with 92+ vulnerability detectors. Trail of Bits. | [GitHub](https://github.com/crytic/slither) |
| **Echidna** | Solidity | Property-based fuzzing for Ethereum smart contracts. Trail of Bits. | [GitHub](https://github.com/crytic/echidna) |
| **EVM MCP Tools** | EVM | Blockchain analysis toolkit for Claude — audit smart contracts, analyze wallets, track profitability, fetch on-chain data via MCP. | [GitHub](https://github.com/0xGval/evm-mcp-tools) |

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

## Agent Frameworks & Toolkits

| Name | Description | Link |
|------|-------------|------|
| **Coinbase AgentKit** | Model-agnostic toolkit giving AI agents crypto wallets and on-chain interactions. Plug-and-play skills: authenticate, fund, send, trade, earn. | [GitHub](https://github.com/coinbase/agentkit) |
| **GOAT (Great Onchain Agent Toolkit)** | Universal adapter between AI agents and any blockchain app. 200+ plugins across 30+ chains. Works with Langchain, Vercel AI SDK, ElizaOS, MCP. | [GitHub](https://github.com/goat-sdk/goat) |
| **ElizaOS** | AI agent framework built for Web3 from day one. Production-proven blockchain integrations, originally launched as ai16z. | [GitHub](https://github.com/elizaOS/eliza) |
| **OpenClaw** | Open-source local-first AI agent framework. 2M+ users, integrates with Claude, GPT, and Web3 skills for wallet management, token swaps, and stablecoin payments. | [openclaw.com](https://openclaw.com) |

## Chain-Specific MCP Servers

| Name | Chain | Description | Link |
|------|-------|-------------|------|
| **Base MCP** | Base | Official — "provides tools to do anything on Base." | [GitHub](https://github.com/base/base-mcp) |
| **Etherscan MCP** | Ethereum | Ethereum blockchain data tools via Etherscan API. | [GitHub](https://github.com/crazyrabbitLTC/mcp-etherscan-server) |
| **eth-mcp** | Ethereum | Direct Ethereum blockchain interaction. | [GitHub](https://github.com/0xKoda/eth-mcp) |
| **QuickNode EVM MCP** | Multi-EVM | Multichain RPC server (Ethereum, Arbitrum, Base, BSC) using Viem. | [quicknode.com](https://www.quicknode.com/guides/ai/evm-mcp-server) |
| **evm-mcp-server** | Multi-EVM | Blockchain services across multiple EVM-compatible networks. | [GitHub](https://github.com/mcpdotdirect/evm-mcp-server) |
| **Strangelove web3-mcp** | Multi-chain | "1 MCP to rule all them chains" — Ethereum, Solana, Cardano, THORChain, XRP, Bitcoin. | [GitHub](https://github.com/strangelove-ventures/web3-mcp) |
| **BSC MCP** | Binance Smart Chain | Token transfers and smart contract interaction on BSC. | [GitHub](https://github.com/TermiX-official/bsc-mcp) |
| **Polygon MCP** | Polygon PoS | On-chain tools for Claude AI on Polygon. | [GitHub](https://github.com/Dablclub/polygon-mcp) |
| **StarkNet MCP** | StarkNet | Query blockchain data, manage wallets, interact with smart contracts. | [GitHub](https://github.com/mcpdotdirect/starknet-mcp-server) |
| **Alchemy SDK MCP** | Multi-chain | Integration with Alchemy SDK for blockchain and NFT operations. | [GitHub](https://github.com/itsanishjain/alchemy-sdk-mcp) |
| **Linea MCP** | Linea | On-chain tools for AI applications on Linea. | [GitHub](https://github.com/qvkare/linea-mcp) |
| **Nodit MCP** | Multi-chain | Structured, context-ready blockchain data. | [GitHub](https://github.com/noditlabs/nodit-mcp-server) |
| **Bankless Onchain MCP** | Multi-chain | Blockchain data interaction through the Bankless API. | [GitHub](https://github.com/Bankless/onchain-mcp) |

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
| **Hyperlane MCP** | Interoperability tooling for interchain AI agents. | [hyperlane.xyz](https://www.hyperlane.xyz/post/introducing-hyperlane-mcp-tooling-for-interchain-agents) |
| **Meson MCP** | Cross-chain transactions for asset transfers. | [GitHub](https://github.com/demcp/demcp-meson-mcp) |
| **Bridge Rates MCP** | Real-time cross-chain bridge rate comparison. | [GitHub](https://github.com/kukapay/bridge-rates-mcp) |

## Wallet & Infrastructure

| Name | Description | Link |
|------|-------------|------|
| **Trust Wallet Skills + MCP** | Claude Code skills marketplace + MCP server for Trust Wallet APIs, chains, and wallet functions. | [developer.trustwallet.com](https://developer.trustwallet.com/developer/claude-code-skills) |
| **Coinbase AgentKit** | Agentic wallets on Base with TEE-isolated private keys. Model-agnostic (Claude, GPT, OpenClaw). | [GitHub](https://github.com/coinbase/agentkit) |
| **Armor Crypto MCP** | Blockchain interaction, swaps, and strategic planning. | [GitHub](https://github.com/armorwallet/armor-crypto-mcp) |
| **Thirdweb MCP** | Query real-time blockchain data on EVM chains, access ABIs and source code, execute transactions. | [blog.thirdweb.com](https://blog.thirdweb.com/changelog/thirdweb-mcp-server-v0-1-beta/) |

## Dev Tools

| Name | Description | Link |
|------|-------------|------|
| **Foundry MCP Server** | Experimental MCP server for Foundry — built for Solidity devs. | [GitHub](https://github.com/PraneshASP/foundry-mcp-server) |
| **Lyra Tool Discovery** | AI-powered automation that discovers MCP servers for you. Point it at GitHub/npm, get ready-to-ship plugin configs. | [GitHub](https://github.com/nirholas/lyra-tool-discovery) |
| **Skill-to-MCP** | Convert AI Skills (Claude Skills format) to MCP server resources. | [GitHub](https://github.com/biocontext-ai/skill-to-mcp) |
| **SpoonOS Web3 Skills** | 57 Python scripts across 19 skills for Web3 integrations (DeFi, NFT, DAO, Security). | [GitHub](https://github.com/XSpoonAi/spoon-awesome-skill) |
| **Web3 Research MCP** | Deep research for crypto — local analysis and research automation. | [GitHub](https://github.com/aaronjmars/web3-research-mcp) |

## Awesome Lists

| Name | Description | Link |
|------|-------------|------|
| **awesome-blockchain-mcps** | Curated list of Blockchain & Crypto MCP servers. | [GitHub](https://github.com/royyannick/awesome-blockchain-mcps) |
| **awesome-crypto-mcp-servers (Hive)** | MCP servers for cryptocurrency, blockchain, and Web3. | [GitHub](https://github.com/hive-intel/awesome-crypto-mcp-servers) |
| **awesome-web3-mcp-servers (DeMCP)** | Decentralized MCP network directory. | [GitHub](https://github.com/demcp/awesome-web3-mcp-servers) |
| **awesome-blockchain-ai** | Curated list of blockchain projects for AI/ML. | [GitHub](https://github.com/steven2358/awesome-blockchain-ai) |
| **awesome-x402** | Resources for x402 HTTP 402 Payment Required protocol — blockchain payments, AI agents, API monetization. | [GitHub](https://github.com/xpaysh/awesome-x402) |

---

## Contributing

PRs welcome! If you know of an Ethereum/Web3 AI skill, MCP server, or agent toolkit not listed here, please open a pull request.

## License

CC0 1.0 Universal
