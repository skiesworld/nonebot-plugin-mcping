from nonebot import on_command, require

require("nonebot_plugin_guild_patch")
from nonebot.plugin import PluginMetadata
from nonebot.internal.matcher import Matcher
from nonebot.internal.params import ArgPlainText
from nonebot.params import CommandArg
from nonebot.adapters import Message
from nonebot.adapters.onebot.v11 import MessageEvent as OBMessageEvent, MessageSegment as OBMessageSegment
from nonebot.adapters.qq import MessageEvent as QQMessageEvent, MessageSegment as QQMessageSegment
from .data_source import get_java_server_status, get_be_server_status

__plugin_meta__ = PluginMetadata(
    name="MC Ping",
    description="获取 Minecraft JE/BE 服务器 Motd 图片信息",
    type="application",
    homepage="https://github.com/MineGraphCN/nonebot-plugin-mcping",
    usage="jes mc.java.com; bes mc.be.com",
    supported_adapters={
        "nonebot.adapters.onebot.v11",
        "nonebot.adapters.qq",
    }
)

jes = on_command("jes", priority=90)
bes = on_command("bes", priority=90)


@jes.handle()
@bes.handle()
async def handle_first_receive(matcher: Matcher, args: Message = CommandArg()):
    plain_text = args.extract_plain_text()
    if plain_text:
        matcher.set_arg("server", args)


@jes.got("server", prompt="你想查询那个服务器的状态呢？")
async def handle_server_ip(
        matcher: Matcher,
        event: OBMessageEvent | QQMessageEvent,
        server_ip: str = ArgPlainText("server")
):
    if server_status := await get_java_server_status(server_ip):
        if isinstance(event, OBMessageEvent):
            server_status = OBMessageSegment.image(server_status.tobytes())
        else:
            server_status = QQMessageSegment.file_image(server_status.tobytes())
        await matcher.finish(server_status)
    else:
        await matcher.finish("查询服务器失败，请稍后再试")


@bes.got("server", prompt="你想查询那个服务器的状态呢？")
async def handle_server_ip(
        matcher: Matcher,
        event: OBMessageEvent | QQMessageEvent,
        server_ip: str = ArgPlainText("server")
):
    if server_status := await get_be_server_status(server_ip):
        if isinstance(event, OBMessageEvent):
            server_status = OBMessageSegment.image(server_status.tobytes())
        else:
            server_status = QQMessageSegment.file_image(server_status.tobytes())
        await matcher.finish(server_status)
