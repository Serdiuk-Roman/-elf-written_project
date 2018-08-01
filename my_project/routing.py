from channels.routing import ProtocolTypeRouter, URLRouter
import news_scrap.routing

application = ProtocolTypeRouter(
    {"websocket": URLRouter(news_scrap.routing.websocket_urlpatterns)}
)
