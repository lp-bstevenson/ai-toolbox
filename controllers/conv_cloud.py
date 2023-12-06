import requests
import logging

log = logging.getLogger(__name__)


def get_le_user(acc: str, id: str, domain: str, authorization: str):
    try:
        url = f"https://{domain}/api/account/{acc}/configuration/le-users/users/{id}?v=5.0&source=db&select=$all"
        headers = {
            "Authorization": f"Bearer {authorization}",
            "Content-Type": "application/json",
        }
        r = requests.get(url=url, headers=headers)
        response = r.json()
        if r.status_code == 200:
            return response
    except Exception as e:
        log.exception(
            f"Exception when attempting to generate completion from LLM Gateway Chat endpoint. Error: {str(e)}"
        )
        raise e


"""
exports.getUser = async (req, res) => {
  const { acc, id } = req.params
  const { domain, authorization } = req.headers
  try {
    const options = {
      method: 'get',
      url: `https://${domain}/api/account/${acc}/configuration/le-users/users/${id}?v=5.0&source=ccuiUmUsers&select=$all`,
      headers: {
        accept: 'application/json',
        'Content-Type': 'application/json; charset=utf-8',
        authorization
      }
    }

    const response = await axios(options)
    console.info(response.data)
    res.status(200).send({
      data: response.data,
      headers: response.headers
    })
  } catch (err) {
    console.info(err.response)
    sendError(res, err)
  }
}
"""  # noqa: E999
