from algosdk import account, mnemonic, transaction
from algosdk.v2client import algod
from algosdk.transaction import Multisig, MultisigTransaction

ALGOD_ADDRESS = "https://testnet-api.algonode.cloud"
ALGOD_TOKEN = ""  # No token required

algod_client = algod.AlgodClient(ALGOD_TOKEN, ALGOD_ADDRESS)

def sign_multisig_txn(msig, sender_mn, receiver, amount):
    params = algod_client.suggested_params()
    txn = transaction.PaymentTxn(msig.address(), params, receiver, amount)
    mtx = MultisigTransaction(txn, msig)

    private_key = mnemonic.to_private_key(sender_mn)
    mtx.sign(private_key)

    return mtx

def combine_and_send(mtx1, signer2_mn):
    mtx1.sign(mnemonic.to_private_key(signer2_mn))
    txid = algod_client.send_raw_transaction(bytes(mtx1))
    transaction.wait_for_confirmation(algod_client, txid, 4)
    print("Transaction ID:", txid)

# Example usage (fill in actual mnemonics and addresses)
# msig = Multisig(1, 2, [addr1, addr2, addr3])
# mtx1 = sign_multisig_txn(msig, sender1_mnemonic, receiver_address, 100000)
# combine_and_send(mtx1, sender2_mnemonic)
