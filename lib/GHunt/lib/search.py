import json
import httpx

from pprint import pprint


def search(query, data_path, gdocs_public_doc, size=1000):
    cookies = ""
    token = ""

    with open(data_path, 'r') as f:
        out = json.loads(f.read())
        token = out["keys"]["gdoc"]
        cookies = out["cookies"]
    data = {
        "request": f'["documentsuggest.search.search_request","{query}",[{size}],null,1]'
    }

    req = httpx.post(
        f'https://docs.google.com/document/d/{gdocs_public_doc}/explore/search?token={token}',
        cookies=cookies,
        data=data,
    )

    if req.status_code != 200:
        exit(f"Error (GDocs): request gives {req.status_code}")

    output = json.loads(req.text.replace(")]}'", ""))
    #pprint(output)
    if isinstance(output[0][1], str) and output[0][1].lower() == "xsrf":
        exit(f"\n[-] Error : XSRF detected.\nIt means your cookies have expired, please generate new ones.")

    results = []
    for result in output[0][1]:
        link = result[0][0]
        title = result[0][1]
        desc = result[0][2]
        results.append({"title": title, "desc": desc, "link": link})

    return results
