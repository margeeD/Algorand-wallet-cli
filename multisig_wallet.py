from algosdk import account, mnemonic
from algosdk.transaction import Multisig, MultisigTransaction

def create_multisig():
    sk1, addr1 = account.generate_account()
    sk2, addr2 = account.generate_account()
    sk3, addr3 = account.generate_account()

    print("Address 1:", addr1)
    print("Mnemonic 1:", mnemonic.from_private_key(sk1))
    print("Address 2:", addr2)
    print("Mnemonic 2:", mnemonic.from_private_key(sk2))
    print("Address 3:", addr3)
    print("Mnemonic 3:", mnemonic.from_private_key(sk3))

    msig = Multisig(version=1, threshold=2, addresses=[addr1, addr2, addr3])
    print("Multisig Address:", msig.address())

if __name__ == "__main__":
    create_multisig()
