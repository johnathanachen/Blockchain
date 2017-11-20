# Blockchain


```bash
$ curl -X POST -H "Content-Type: application/json" -d '{
 "sender": "d4ee26eee15148ee92c6cd394edd974e",
 "recipient": "someone-other-address",
 "amount": 5
}' "http://localhost:5000/transactions/new"
```
```bash
$ curl -X POST -H "Content-Type: application/json" -d '{
"nodes": ["http://localhost:5001"]
}' "http://localhost:5000/nodes/register"
```
