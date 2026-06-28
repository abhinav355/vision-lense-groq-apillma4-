from groq import Groq
import webview


class VisionLense:

    def __init__(self):
        self.client = None

    def set_api_key(self, api_key):
        self.client = Groq(api_key=api_key)
        return {"success": True}

    def analyze_image(self, image_data):
        try:
            if not self.client:
                return {"success": False, "error": "API key not set"}

            image_base64 = image_data.split(",")[1]

            completion = self.client.chat.completions.create(
                model="meta-llama/llama-4-scout-17b-16e-instruct",
                messages=[
                    {
                        "role": "user",
                        "content": [
                            {
                                "type": "text",
                                "text": "describe everything in this image in detail if a persone shows a product with their tounge out say product mode and describe the product only"
                            },
                            {
                                "type": "image_url",
                                "image_url": {
                                    "url": f"data:image/jpeg;base64,{image_base64}"
                                }
                            }
                        ]
                    }
                ],
                temperature=0.2,
                max_completion_tokens=500
            )

            return {
                "success": True,
                "result": completion.choices[0].message.content
            }

        except Exception as error:
            return {
                "success": False,
                "error": str(error)
            }



api = VisionLense()

webview.create_window(
    title="VisionLense",
    url="UI.html",
    js_api=api,
    width=1400,
    height=900
)

webview.start()
