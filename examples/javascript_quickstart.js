/**
 * fault.bet API — JavaScript / Node.js quickstart
 *
 * Fetches today's pre-match signals from the fault.bet API and prints them.
 *
 * Get an API key at: https://fault.bet/api
 * Docs: https://fault.bet/api
 *
 * Run: node javascript_quickstart.js
 */

// Get your API key from https://fault.bet/api after subscribing.
// Set as environment variable: export FAULTBET_API_KEY="fb_..."
const API_KEY = process.env.FAULTBET_API_KEY || "YOUR_FAULTBET_API_KEY_HERE";
const BASE_URL = "https://api.fault.bet";

async function fetchTodaysSignals() {
  try {
    const res = await fetch(`${BASE_URL}/v1/signals/today`, {
      headers: {
        "Authorization": `Bearer ${API_KEY}`,
        "Accept": "application/json",
      },
    });
    if (!res.ok) {
      console.error(`HTTP ${res.status}: ${res.statusText}`);
      if (res.status === 401) {
        console.error("Check your FAULTBET_API_KEY — see https://fault.bet/api");
      }
      return null;
    }
    return await res.json();
  } catch (err) {
    console.error(`Connection error: ${err.message}`);
    return null;
  }
}

async function main() {
  const data = await fetchTodaysSignals();
  if (!data) return;

  const signals = data.signals || [];
  console.log(`fault.bet — ${signals.length} signals for today`);
  console.log("=".repeat(70));

  for (const s of signals) {
    const match = `${s.player1_name} vs ${s.player2_name}`;
    console.log(`\n  ${match}`);
    console.log(`    Tournament:  ${s.tournament || ""}`);
    console.log(`    BACK:        ${s.back_player} @ ${s.market_price}`);
    console.log(`    Edge:        +${(s.edge_pct || 0).toFixed(1)}%`);
    console.log(`    Confidence:  ${s.confidence}/100`);
    console.log(`    Stake:       ${(s.suggested_stake_pct || 0).toFixed(2)}% bank`);
  }
}

main();
