import pytest


def parse_interfaces(output: str):
    result = []
    if output == "" or output is None:
        return result
    for line in output.strip().splitlines()[1:]:
        name, ip, status, protocol = line.split()
        result.append({
            "name": name,
            "ip": ip if ip != "unassigned" else None,
            "status": status,
            "protocol": protocol
        })

    return result


@pytest.mark.parametrize("output, result", [
    (
            """
            Interface    IP-Address     Status   Protocol
            Gi0/1        10.0.0.1       up       up
            Gi0/2        unassigned     down     down
            """,
            [{
                "name": "Gi0/1",
                "ip": "10.0.0.1",
                "status": "up",
                "protocol": "up"
            },{
                "name": "Gi0/2",
                "ip": None,
                "status": "down",
                "protocol": "down"
            }
            ]
    ),(
            """
            Interface    IP-Address     Status   Protocol
            """,
            []
    )
])
def test_output_validation(output, result):
    assert parse_interfaces(output) == result


if __name__ == '__main__':
    test_output_validation()
