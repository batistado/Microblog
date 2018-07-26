class Serializer:
    @staticmethod
    def serialize_post(post):
        return {
            'author': {
                'username': post.username,
            },
            'body': post.body,
        }
