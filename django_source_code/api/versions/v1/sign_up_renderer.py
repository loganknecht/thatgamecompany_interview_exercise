# Python Standard Libraries
import json
# Third-Party Libraries
from rest_framework.renderers import JSONRenderer
# Custom Libraries
# N/A


class SignUpJSONRenderer(JSONRenderer):
    charset = "utf-8"

    def render(self, data, media_type=None, renderer_context=None):
        # If we receive a `token` key as part of the response, it will be a
        # byte object. Byte objects don"t serialize well, so we need to
        # decode it before rendering the User object.
        token = data.get("token", None)

        if(token is not None and
                isinstance(token, bytes)):
            # Also as mentioned above, we will decode `token` if it is of type
            # bytes.
            data["token"] = token.decode("utf-8")

        render_data = json.dumps({
            "user": data
        })

        return render_data
