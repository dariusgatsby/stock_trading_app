import os

from sinch import Client


def send_message(text: str):
    sinch_client = Client(
        key_id="8a1c28ac-5327-464b-9577-99465dfc3496",
        key_secret=os.environ.get("SINCH_API_KEY"),
        project_id="3215f976-9e0a-43bd-93b4-1478470a907b"
    )

    send_batch_response = sinch_client.sms.batches.send(
        body=text,
        to=["+12133003141"],
        from_="12066578354",
        delivery_report="none"
    )

    print(send_batch_response)


if __name__ == "__main__":
    print("ello,govna")
