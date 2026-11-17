import pytest

from parser import parse_interfaces


@pytest.mark.parametrize("output, expected", [
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
            }, {
                "name": "Gi0/2",
                "ip": None,
                "status": "down",
                "protocol": "down"
            }
            ]
    ), (
            """
            Interface    IP-Address     Status   Protocol
            """,
            []
    ), (
            """
            Interface    IP-Address     Status   Protocol
            
            Gi0/2        unassigned     down     down
            """,
            [{
                "name": "Gi0/2",
                "ip": None,
                "status": "down",
                "protocol": "down"
            }]
    )
])
def test_output_validation(output, expected):
    assert parse_interfaces(output) == expected
