from boa.interop.System.Runtime import Notify, Serialize, Deserialize
from boa.interop.System.Storage import Get, Put, GetContext

NUM_LIST_KEY = "key1"
ACCOUNT_LIST_KEY = "key2"

def Main(operation, args):
    if operation == "checkList":
        numberList = args[0]
        accountList = args[1]
        return checkList(numberList, accountList)
    return False

def checkList(numberList, accountList):

    Notify(["111", numberList, accountList])
    numberListInfo = Serialize(numberList)
    Put(GetContext(), NUM_LIST_KEY, numberListInfo)
    accountListInfo = Serialize(accountList)
    Put(GetContext(), ACCOUNT_LIST_KEY, accountListInfo)

    numberListInfo1 = Get(GetContext(), NUM_LIST_KEY)
    numberList1 = Deserialize(numberListInfo1)
    accountListInfo1 = Get(GetContext(), ACCOUNT_LIST_KEY)
    accountList1 = Deserialize(accountListInfo1)
    Notify(["222", numberList1, accountList1])
    return [numberList, accountList]

