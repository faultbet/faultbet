# fault.bet API — Examples

Quick-starts for the [fault.bet](https://fault.bet) tennis-trading signals API.

## Get an API key

Subscribe to an API plan at [fault.bet/api](https://fault.bet/api). Your key (starting with `fb_`) is emailed immediately after checkout. Free preview tier in development.

## Set your API key

```bash
export FAULTBET_API_KEY="fb_your_actual_key_here"
```

Don't hard-code keys into source files. Don't commit them. The `.gitignore` in this repo blocks `.env` files by default — keep it that way.

## Quick-starts

- **Python**: [`python_quickstart.py`](python_quickstart.py)
  ```bash
  python3 python_quickstart.py
  ```

- **JavaScript / Node**: [`javascript_quickstart.js`](javascript_quickstart.js)
  ```bash
  node javascript_quickstart.js
  ```

Both fetch today's pre-match signals and print them in a readable format.

## Endpoints used in these examples

- `GET /v1/signals/today` — today's pre-match signals (8%+ edge, Betfair-confirmed)

Full endpoint list, rate limits, and response shapes at [fault.bet/api](https://fault.bet/api).

## Issues / questions

Open an [issue](https://github.com/faultbet/faultbet/issues) or email [hello@fault.bet](mailto:hello@fault.bet).
