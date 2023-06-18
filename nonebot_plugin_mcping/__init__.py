from nonebot import on_command
from nonebot.plugin import PluginMetadata
from nonebot.internal.matcher import Matcher
from nonebot.internal.params import ArgPlainText
from nonebot.params import CommandArg
from nonebot.adapters import Message
from .data_source import get_java_server_status, get_be_server_status

__plugin_meta__ = PluginMetadata(
    name="MC Ping",
    description="获取 Minecraft JE/BE 服务器 Motd 图片信息",
    type="application",
    homepage="https://github.com/17TheWord/nonebot-plugin-mcping",
    usage="jes mc.java.com; bes mc.be.com",
)

jes = on_command("jes", priority=1)
bes = on_command("bes", priority=1)


@jes.handle()
async def handle_first_receive(matcher: Matcher, args: Message = CommandArg()):
    plain_text = args.extract_plain_text()
    if plain_text:
        matcher.set_arg("server", args)


@bes.handle()
async def handle_first_receive(matcher: Matcher, args: Message = CommandArg()):
    plain_text = args.extract_plain_text()
    if plain_text:
        matcher.set_arg("server", args)


@jes.got("server", prompt="你想查询那个服务器的状态呢？")
async def handle_city(server_ip: str = ArgPlainText("server")):
    server_status = await get_java_server_status(server_ip)
    await jes.finish(server_status)


@bes.got("server", prompt="你想查询那个服务器的状态呢？")
async def handle_city(server_ip: str = ArgPlainText("server")):
    server_status = await get_be_server_status(server_ip)
    await bes.finish(server_status)
