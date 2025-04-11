class BaseTransformer:
    def transform(self, code):
        raise NotImplementedError("Each transformer must implement the transform method.")
