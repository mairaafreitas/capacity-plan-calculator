from support.utils import kb_to_mb


def calculate_bandwith(requests_per_second: int, request_size: int):
    """Calculate the Bandwith required for the requests."""
    print("\n======Bandwith======")
    print("Bandwith = Requests per second * Average request size")

    bandwith_kb = round(requests_per_second * request_size, 4)
    bandwith_mb = round(kb_to_mb(bandwith_kb), 4)
    print(f"The Bandwith required for the requests is: {bandwith_kb}kbs")
    print(f"The Bandwith required for the requests is: {bandwith_mb}mbs")
