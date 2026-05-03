"""
fault.bet API — Python quickstart

Fetches today's pre-match signals from the fault.bet API and prints them.

Get an API key at: https://fault.bet/api
Docs: https://fault.bet/api
"""
import os
import json
import urllib.request
import urllib.error

# Get your API key from https://fault.bet/api after subscribing.
# Set as environment variable: export FAULTBET_API_KEY="fb_..."
API_KEY = os.environ.get("FAULTBET_API_KEY", "YOUR_FAULTBET_API_KEY_HERE")
BASE_URL = "https://api.fault.bet"


def fetch_todays_signals():
    """Fetch today's published pre-match signals."""
    req = urllib.request.Request(
        f"{BASE_URL}/v1/signals/today",
        headers={
            "Authorization": f"Bearer {API_KEY}",
            "Accept": "application/json",
        },
    )
    try:
        with urllib.request.urlopen(req, timeout=10) as resp:
            return json.loads(resp.read())
    except urllib.error.HTTPError as e:
        print(f"HTTP {e.code}: {e.reason}")
        if e.code == 401:
            print("Check your FAULTBET_API_KEY — see https://fault.bet/api")
        return None
    except urllib.error.URLError as e:
        print(f"Connection error: {e.reason}")
        return None


def main():
    signals = fetch_todays_signals()
    if not signals:
        return

    print(f"fault.bet — {len(signals.get('signals', []))} signals for today")
    print("=" * 70)

    for s in signals.get("signals", []):
        edge = s.get("edge_pct", 0)
        conf = s.get("confidence", 0)
        price = s.get("market_price", 0)
        player = s.get("back_player", "?")
        match = f"{s.get('player1_name')} vs {s.get('player2_name')}"
        tournament = s.get("tournament", "")

        print(f"\n  {match}")
        print(f"    Tournament:  {tournament}")
        print(f"    BACK:        {player} @ {price}")
        print(f"    Edge:        +{edge:.1f}%")
        print(f"    Confidence:  {conf}/100")
        print(f"    Stake:       {s.get('suggested_stake_pct', 0):.2f}% bank")


if __name__ == "__main__":
    main()
