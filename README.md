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
- [Cross-Chain & Bridge MCP Servers](#cross-chain--bridge-mcp-servers)
- [Wallet & Infrastructure](#wallet--infrastructure)
- [Standards & Identity](#standards--identity)
- [Frontend & Social](#frontend--social)
- [Awesome Lists & Directories](#awesome-lists--directories)
- [Discovery Resources](#discovery-resources)

---

## Knowledge & Skill Registries

Everything you need to get started — foundational Ethereum and crypto knowledge packaged as AI skills.

| Name | Description | Link |
|------|-------------|------|
| **ETHSKILLS** | Modular Ethereum knowledge for AI agents — gas, L2s, standards, security, DeFi, auditing, and more. No install required. Built by Austin Griffith / BuidlGuidl / Ethereum Foundation. | [ethskills.com](https://ethskills.com/) |
| **CryptoSkills** | 97+ production-ready AI agent skills across 14 categories and 15 blockchains. Covers DeFi protocols (Aave, Compound, Curve, Lido, Pendle, GMX, etc.), L2s (Arbitrum, Base, Optimism, StarkNet, etc.), oracles (Chainlink, Pyth, RedStone), security tools, cross-chain bridges, dev frameworks, and more. Install via `npx cryptoskills install`. | [cryptoskills.dev](https://cryptoskills.dev/) |
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

## Exchange & Trading Skills

| Name | Platform | Description | Link |
|------|----------|-------------|------|
| **Binance AI Agent Skills** | Binance | 11 modular skills for spot trading, derivatives, margin, market intelligence, token auditing, asset management, and Binance Alpha data. | [binance.com](https://www.binance.com/en/support/announcement/detail/bafb9dda6cbb47d5882a4090c31d4c64) |
| **Bybit AI Skills** | Bybit | 253 API endpoints — market intelligence, spot trading, derivatives, earn products, account management. Works with ChatGPT, Claude, OpenClaw, Cursor. | [chainwire.org](https://chainwire.org/2026/03/13/bybit-launches-ai-skills-powering-ai-agents-for-crypto-trading-with-zero-setup-253-api-endpoints-and-growing/) |
| **KuCoin Skills Hub** | KuCoin | Open skills marketplace for AI-driven crypto access — market data, analytics, trading signals. Expanding to wallet ops, staking, lending, and yield. | [kucoin.com](https://www.kucoin.com/announcement/en-kucoin-skills-hub-is-now-live-connecting-ai-agents-to-the-kucoin-exchange) |
| **Bitget Wallet Skill** | Bitget | AI agent suite for onchain market data, trading infrastructure, and blockchain data via natural language. | [bitcoinethereumnews.com](https://bitcoinethereumnews.com/tech/bitget-wallet-expands-into-ai-agent-capabilities-with-skill-beta/) |

## Smart Contract Security

| Name | Focus | Description | Link |
|------|-------|-------------|------|
| **ETHSKILLS Audit** | Solidity | 500+ item contract audit system with specialist agents. | [ethskills.com](https://ethskills.com/) |
| **QuillShield** | Solidity | AI-powered vulnerability detection that learns from past exploits, reduces false positives. | [quillaudits.com](https://www.quillaudits.com/) |
| **EVM MCP Tools** | EVM | Blockchain analysis toolkit for Claude — audit smart contracts, analyze wallets, track profitability, fetch on-chain data via MCP. | [GitHub](https://github.com/0xGval/evm-mcp-tools) |
| **SecSkills Web3** | Web3 Security | Security-first Web3 development for Ethereum and EVM chains. | [LobeHub](https://lobehub.com/skills/trilwu-secskills-web3-blockchain) |

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
| **Web3 Research MCP** | Crypto research | Deep research for crypto — local analysis and research automation. | [GitHub](https://github.com/aaronjmars/web3-research-mcp) |

## Agent Frameworks & Toolkits

| Name | Description | Link |
|------|-------------|------|
| **Coinbase AgentKit** | Model-agnostic toolkit giving AI agents crypto wallets and on-chain interactions. Plug-and-play skills: authenticate, fund, send, trade, earn. TEE-isolated private keys on Base. | [GitHub](https://github.com/coinbase/agentkit) |
| **GOAT (Great Onchain Agent Toolkit)** | Universal adapter between AI agents and any blockchain app. 200+ plugins across 30+ chains. Works with Langchain, Vercel AI SDK, ElizaOS, MCP. | [GitHub](https://github.com/goat-sdk/goat) |
| **ElizaOS** | AI agent framework built for Web3 from day one. Production-proven blockchain integrations, originally launched as ai16z. | [GitHub](https://github.com/elizaOS/eliza) |
| **OpenClaw** | Open-source local-first AI agent framework. 2M+ users, integrates with Claude, GPT, and Web3 skills for wallet management, token swaps, and stablecoin payments. | [openclaw.com](https://openclaw.com) |
| **eth-agent** | TypeScript library giving AI agents a simple, safe interface to send stablecoins (USDC/USDT/DAI) and ETH across chains. | [LobeHub](https://lobehub.com/skills/lambdaclass-eth-agent-eth-agent) |
| **SpoonOS Web3 Skills** | 57 Python scripts across 19 skills for Web3 integrations (DeFi, NFT, DAO, Security). | [GitHub](https://github.com/XSpoonAi/spoon-awesome-skill) |
| **Skill-to-MCP** | Convert AI Skills (Claude Skills format) to MCP server resources. | [GitHub](https://github.com/biocontext-ai/skill-to-mcp) |
| **Lyra Tool Discovery** | AI-powered automation that discovers MCP servers for you. Point it at GitHub/npm, get ready-to-ship plugin configs. | [GitHub](https://github.com/nirholas/lyra-tool-discovery) |

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
| **Foundry MCP Server** | Ethereum | Experimental MCP server for Foundry — built for Solidity devs. | [GitHub](https://github.com/PraneshASP/foundry-mcp-server) |

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

## Cross-Chain & Bridge MCP Servers

| Name | Description | Link |
|------|-------------|------|
| **Wormhole MCP** | Automatic token transfers across multiple blockchains via Wormhole SDK. | [GitHub](https://github.com/collinsezedike/wormhole-mcp) |
| **Meson MCP** | Cross-chain transactions for asset transfers. | [GitHub](https://github.com/demcp/demcp-meson-mcp) |

## Wallet & Infrastructure

| Name | Description | Link |
|------|-------------|------|
| **Trust Wallet Skills + MCP** | Claude Code skills marketplace + MCP server for Trust Wallet APIs, chains, and wallet functions. | [developer.trustwallet.com](https://developer.trustwallet.com/developer/claude-code-skills) |
| **Armor Crypto MCP** | Blockchain interaction, swaps, and strategic planning. | [GitHub](https://github.com/armorwallet/armor-crypto-mcp) |
| **Thirdweb MCP** | Query real-time blockchain data on EVM chains, access ABIs and source code, execute transactions. | [blog.thirdweb.com](https://blog.thirdweb.com/changelog/thirdweb-mcp-server-v0-1-beta/) |
| **Vincent Wallet** | Secure EVM wallet for agent transfers, swaps, and transactions. | [GitHub](https://github.com/HeyVincent-ai/agent-skills/tree/main/wallet) |
| **Vincent Polymarket** | Polymarket prediction market trading for agents. | [GitHub](https://github.com/HeyVincent-ai/agent-skills/tree/main/polymarket) |
| **AgentFund Skill** | Crowdfunding for AI agents on Base chain — milestone escrow. | [GitHub](https://github.com/RioBot-Grind/agentfund-skill) |
| **CryptoWallet (OpenClaw)** | Multi-chain wallet management — 12 EVM networks. | [LobeHub](https://lobehub.com/skills/openclaw-skills-cryptowallet) |

## Standards & Identity

| Name | Description | Link |
|------|-------------|------|
| **ERC-8004** | Onchain agent identity standard — deployed on 20+ chains. Co-led by Ethereum Foundation, MetaMask, and Google. | [ethereum.org](https://ethereum.org/ai-agents/) |

## Frontend & Social

| Name | Description | Link |
|------|-------------|------|
| **Ethereum-Wingman** | Ethereum development tutor for Scaffold-ETH 2 — fork-mode testing against live protocols. | [LobeHub](https://lobehub.com/skills/openclaw-skills-ethereum-wingman) |
| **Web3 Community Skill** | Web3 community management and engagement patterns. | [LobeHub](https://lobehub.com/skills/omer-metin-skills-for-antigravity-web3-community) |
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
