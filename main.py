"""make.fun bounty news-summary-01.

Writes a fixed English summary of the world's news of Wednesday
11 November 2026 to /output/entry.txt.

Deterministic and offline: no network, no randomness, no dates or
other varying input. Running it twice writes identical bytes.
"""

from pathlib import Path

SUMMARY = (
    "On Wednesday 11 November 2026, Washington moved to end the longest "
    "federal shutdown in American history. The House passed a funding "
    "package 222-209, ending 43 days of closure, funding most of the "
    "government through 30 January, though it left expiring health-care "
    "subsidies unresolved.\n"
    "\n"
    "In Abu Dhabi, two days of US-mediated talks between Russia and "
    "Ukraine ended with agreement in principle to the largest prisoner "
    "exchange yet, possibly 1,000 to 1,500 on each side, but no ceasefire "
    "or territorial deal. Envoys Jared Kushner and Steve Witkoff were due "
    "to meet Vladimir Putin next.\n"
    "\n"
    "NATO jets scrambled after at least four drones entered Baltic "
    "airspace overnight, while a drone strike set fire to Russia's "
    "Ust-Luga port. In the Strait of Hormuz, shipping attacks pushed oil "
    "higher, Brent rising to $92.53, as the US said sanctions were "
    "devastating Iran and major combat was no longer needed.\n"
    "\n"
    "At COP31 in Antalya, UN chief Antonio Guterres warned that the "
    "climate crisis was outrunning humanity, calling it a path to mutually "
    "assured destruction. In Gaza, Israeli strikes killed three people, "
    "and the UN said more than 150,000 aid tents were held outside Gaza "
    "as floods swamped shelters.\n"
    "\n"
    "In business, a Reuters investigation found a blacklisted Chinese "
    "university had bought two Nvidia H200 chips, while Anthropic set its "
    "IPO price range at $70 to $78 a share, with Nvidia and Google each "
    "agreeing to buy about $10 billion of stock. In Italy, hoax bomb "
    "threats evacuated at least 300 schools."
)


def main() -> None:
    output = Path("/output/entry.txt")
    try:
        output.parent.mkdir(parents=True, exist_ok=True)
        output.write_text(SUMMARY, encoding="utf-8")
    except OSError:
        # Local fallback when /output is not writable (e.g. running
        # outside the competition runner). The bytes written are identical.
        fallback = Path("output/entry.txt")
        fallback.parent.mkdir(parents=True, exist_ok=True)
        fallback.write_text(SUMMARY, encoding="utf-8")


if __name__ == "__main__":
    main()
