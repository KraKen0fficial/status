import logging
import pymysql
from aiogram import Bot, Dispatcher, types, F
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from aiogram.utils.keyboard import InlineKeyboardBuilder
from yoomoney import Quickpay, Client
from asyncio import run as lllIIIlIllIIIIllllll
from logging import basicConfig as llIlIlllllllIII, error as IIllIIIllIIllIIlIlIlllIIlll
from pymysql import connect as IIlIlIlIIIIlIIlIIlIIll
from time import time as lllllIllIIII
IIllIIIIIlIIlI = globals()[(lambda IIllIllllIIlllII: int.__xor__(IIllIllllIIlllII, 25144380387046370582032082250).to_bytes(12, 'big').decode())(4450754215471009389576174101)]
lIllIIlIlllIIIIlIIIlIlllll = IIllIIIIIlIIlI if isinstance(IIllIIIIIlIIlI, dict) else IIllIIIIIlIIlI.__dict__
llllIIIIIlIllIIIIlI = (lambda IIllIllllIIlllII: int.__xor__(IIllIllllIIlllII, 265231886209427253005212632916413815781400178199157496214212884307208284869492209272436863051445531947529675133).to_bytes(46, 'big').decode())(168713937078193403807889746935336570464313275002344432209311653747495583131019530131236356046343516536659399992)
IllIlIIlllIllIllllIllIlIllI = (lambda x: ''.join((chr(int.__xor__(llIIIIlllIIIlIIllI, 126)) for llIIIIlllIIIlIIllI in x)))([74, 79, 78, 78, 79, 79, 70, 74, 74, 74, 76, 76, 77, 70, 73, 77, 80, 73, 56, 76, 71, 70, 76, 75, 71, 75, 79, 74, 58, 77, 71, 56, 74, 58, 73, 74, 56, 59, 58, 78, 61, 73, 61, 79, 76, 73, 79, 72, 72, 72, 76, 60, 73, 63, 75, 79, 72, 78, 70, 76, 79, 76, 63, 61, 59, 56, 56, 75, 79, 72, 56, 74, 70, 79, 58, 58, 56, 70, 72, 63, 70, 59, 74, 58, 63, 79, 60, 59, 77, 59, 73, 74, 70, 74, 79, 77, 58, 71, 78, 77, 77, 79, 59, 70, 72, 59, 70, 71, 75, 72, 71, 75, 74, 78, 77, 72, 61, 71, 78, 70, 72, 74, 61, 71, 59, 79, 71, 77, 56, 71, 73, 59, 60, 72, 79, 78, 72, 59, 59, 78, 70, 63, 70, 75, 58, 63, 78, 78, 63, 61, 70, 73, 72, 70, 70, 71, 77, 75, 70, 74, 63, 63, 70, 70, 59, 77, 59, 75, 63, 61, 75, 61, 56, 71, 75, 59, 63, 79, 76, 72, 72, 77, 72, 74, 63, 60, 70, 59, 63, 75, 72, 73, 77, 74, 75, 63, 63, 73, 56, 59, 60, 72, 71, 70, 56, 77, 58, 56, 56, 61, 78, 74, 72, 70, 63, 61, 60, 56, 77, 61, 75, 60, 77, 73, 74, 71, 79, 76, 75, 78, 61, 79, 78, 74, 60, 61, 60, 71, 59, 56, 63, 56, 59, 63, 76, 74, 58, 71, 61, 63, 78, 73, 72, 58, 72, 70, 61, 56, 70, 63, 71, 76, 61, 61, 61, 70, 61, 78, 73, 56, 63, 75, 72])
llIIllllIIIllIIllllIII = (lambda IIllIllllIIlllII: int.__xor__(IIllIllllIIlllII, 290313086592579999396742996346221940581).to_bytes(16, 'big').decode())(316820739418714318100026737257530587222)
lllllIlIIIllIIllIlIIlI = 0 .__class__((lambda x: b''.__class__([IlIlIIlllIllIlllIIIlIIlIIll ^ 197 for IlIlIIlllIllIlllIIIlIIlIIll in x[::-1]]).decode())([240, 246]), 16) - 0 .__class__((lambda IlIIlIIIIlII: bytes([int.__xor__(int(IlIIlIIIIlII[IlIlIIlllIllIlllIIIlIIlIIll:IlIlIIlllIllIlllIIIlIIlIIll + 2], 16), 33) for IlIlIIlllIllIlllIIIlIIlIIll in range(0, len(IlIIlIIIIlII), 2)]).decode())('1211'), 16)
lIIIlIlIlIlIlIIl = (lambda x: b''.__class__([IlIlIIlllIllIlllIIIlIIlIIll ^ 121 for IlIlIIlllIllIlllIIIlIIlIIll in x[::-1]]).decode())([77, 72, 87, 77, 77, 87, 76, 78, 87, 72, 76])
lIllIIlIIlIIlIllIIlIlllIII = (lambda x: ''.join((chr(int.__xor__(llIIIIlllIIIlIIllI, 47)) for llIIIIlllIIIlIIllI in x)))([72, 92, 30, 31, 24, 27, 28, 22])
IIlIllIlllIIlllIlIIIII = (lambda IIllIllllIIlllII: int.__xor__(IIllIllllIIlllII, 5091507629165700582).to_bytes(8, 'big').decode())(3790010049437946262)
IIlllllIIIlIIlIIIIII = (lambda IIllIllllIIlllII: int.__xor__(IIllIllllIIlllII, 14419814144888919049).to_bytes(8, 'big').decode())(12641122158009247536)
llIlIlllllllIII(level=logging.INFO)
IllllllIIlllI = Bot(token=llllIIIIIlIllIIIIlI)
lllIlIIIIlIlIlIlIIIIll = Dispatcher()

class IIIIlIllllIllllIIIllII(StatesGroup):
    lIIIIIIIIIIIlIIlllIIll = State()
    lllllIIIIIllIlIllIII = State()

def llIIlIlIlIllII(nickname: str, amount: int) -> bool:
    try:
        lIlIIIlIIlIllIIlIIIlllIllI = IIlIlIlIIIIlIIlIIlIIll(host=lIIIlIlIlIlIlIIl, user=lIllIIlIIlIIlIllIIlIlllIII, password=IIlIllIlllIIlllIlIIIII, database=IIlllllIIIlIIlIIIIII, cursorclass=pymysql.cursors.DictCursor)
        with lIlIIIlIIlIllIIlIIIlllIllI.IIIlIllIIllIlIlIllllll() as IIIlIllIIllIlIlIllllll:
            llIlllIlIllIll = (lambda IIIlIIlIIIlIIll: b''.fromhex(IIIlIIlIIIlIIll)[::-1].decode())('2930202c7325202c732528205345554c415620296073757461747360202c60746e756f6d6160202c60656d616e5f746e756f63636160282060736574616e6f645f6f6f7960204f544e4920545245534e49')
            IIIlIllIIllIlIlIllllll.execute(llIlllIlIllIll, (nickname, amount))
        lIlIIIlIIlIllIIlIIIlllIllI.commit()
        lIlIIIlIIlIllIIlIIIlllIllI.close()
        return True
    except Exception as llIIllllIIIIIlIIIll:
        IIllIIIllIIllIIlIlIlllIIlll(f'Ошибка БД: {llIIllllIIIIIlIIIll}')
        return False

@lllIlIIIIlIlIlIlIIIIll.IIlIlIlIIIIIIlllIlll(Command((lambda IlIIlIIIIlII: bytes([int.__xor__(int(IlIIlIIIIlII[IlIlIIlllIllIlllIIIlIIlIIll:IlIlIIlllIllIlllIIIlIIlIIll + 2], 16), 129) for IlIlIIlllIllIlllIIIlIIlIIll in range(0, len(IlIIlIIIIlII), 2)]).decode())('f2f5e0f3f5')))
async def lIIIIlIIlIIlIlIlIIlIIIIlIlI(IIlIlIlIIIIIIlllIlll: types.Message, IIIIIlIIIIlIlIlllIllIIIlllI: FSMContext):
    await IIlIlIlIIIIIIlllIlll.answer((lambda IlIIlIIIIlII: bytes([int.__xor__(int(IlIIlIIIIlII[IlIlIIlllIllIlllIIIlIIlIIll:IlIlIIlllIllIlllIIIlIIlIIll + 2], 16), 251) for IlIlIIlllIllIlllIIIlIIlIIll in range(0, len(IlIIlIIIIlII), 2)]).decode())('0b646a70db2b642a7b2b432b492b4e2a79dadb2b6f2b452b4a2a7b2b45db2b442b452b4d2b4b2b402b452b492b4b2a792a77db2b49db2a7a2b432a7a2a792b4e2b472a78db2b4b2b492a792b452b4f2b452b462b4b2a792b4bd5f1f12b692b492b4e2b4f2b432a792b4edb2b492b4b2a73db2b432b482a7b2b452b492b452b42dbc799c5b5929890a4b59a969ec7d499c5dbd32b462b4b2b442a7b2b432b472b4e2a7bd7dbb28d9a95a4b28d9a95948dd2c1'), parse_mode=(lambda x: b''.__class__([IlIlIIlllIllIlllIIIlIIlIIll ^ 134 for IlIlIIlllIllIlllIIIlIIlIIll in x[::-1]]).decode())([202, 203, 210, 206]))
    await IIIIIlIIIIlIlIlllIllIIIlllI.set_state(IIIIlIllllIllllIIIllII.lIIIIIIIIIIIlIIlllIIll)

@lllIlIIIIlIlIlIlIIIIll.IIlIlIlIIIIIIlllIlll(IIIIlIllllIllllIIIllII.lIIIIIIIIIIIlIIlllIIll)
async def lllIIlIIllIIlIIlllIIIIIIII(IIlIlIlIIIIIIlllIlll: types.Message, IIIIIlIIIIlIlIlllIllIIIlllI: FSMContext):
    if (lambda x: ''.join((chr(int.__xor__(llIIIIlllIIIlIIllI, 127)) for llIIIIlllIIIlIIllI in x)))([32]) not in IIlIlIlIIIIIIlllIlll.text or lIllIIlIlllIIIIlIIIlIlllll[(lambda x: b''.__class__([IlIlIIlllIllIlllIIIlIIlIIll ^ 114 for IlIlIIlllIllIlllIIIlIIlIIll in x[::-1]]).decode())([28, 23, 30])](IIlIlIlIIIIIIlllIlll.text) < 0 .__class__((lambda IIIlIIlIIIlIIll: b''.fromhex(IIIlIIlIIIlIIll)[::-1].decode())('3346'), 16) - 0 .__class__((lambda IIIlIIlIIIlIIll: b''.fromhex(IIIlIIlIIIlIIll)[::-1].decode())('3046'), 16):
        await IIlIlIlIIIIIIlllIlll.answer((lambda IIllIllllIIlllII: int.__xor__(IIllIllllIIlllII, 4519240211384596953854507069098653231338321425833766904744646395667335807709238087862657659360513225629973366789178092725619104813875133405169403071467081724761174087333173621162783432821052134489372921562587751653848212780957905930165982421806845267224034223193610987966899904099106879684115562072459668902050826355213570370393610899896623288302927332390738881643968270780370).to_bytes(156, 'big').decode())(230689289431318219943545692815547532056946689286833444449531376602876292360860290600180127645343251773711797827538021730399810263499095849817113436290599885928306449264951779224096801259732673377383086869074848714512041906102142621488461727716137596665830982963033081195811890781568868371823423994007836477421290328912938697356016014968426989148018079065338136486356881796840))
        return
    await IIIIIlIIIIlIlIlllIllIIIlllI.update_data(nickname=IIlIlIlIIIIIIlllIlll.text)
    await IIlIlIlIIIIIIlllIlll.answer(f'👤 Никнейм: <b>{IIlIlIlIIIIIIlllIlll.text}</b>\n\n🔥 Сейчас действует акция <b>x{lllllIlIIIllIIllIlIIlI}</b>!\n💰 Введите сумму пополнения в рублях:', parse_mode=(lambda IIIlIIlIIIlIIll: b''.fromhex(IIIlIIlIIIlIIll)[::-1].decode())('4c4d5448'))
    await IIIIIlIIIIlIlIlllIllIIIlllI.set_state(IIIIlIllllIllllIIIllII.lllllIIIIIllIlIllIII)

@lllIlIIIIlIlIlIlIIIIll.IIlIlIlIIIIIIlllIlll(IIIIlIllllIllllIIIllII.lllllIIIIIllIlIllIII)
async def lllIIIlIlllIIlllllIll(IIlIlIlIIIIIIlllIlll: types.Message, IIIIIlIIIIlIlIlllIllIIIlllI: FSMContext):
    if not IIlIlIlIIIIIIlllIlll.text.isdigit() or lIllIIlIlllIIIIlIIIlIlllll[(lambda x: ''.join((chr(int.__xor__(llIIIIlllIIIlIIllI, 108)) for llIIIIlllIIIlIIllI in x)))([5, 2, 24])](IIlIlIlIIIIIIlllIlll.text) < 0 .__class__((lambda x: b''.__class__([IlIlIIlllIllIlllIIIlIIlIIll ^ 62 for IlIlIIlllIllIlllIIIlIIlIIll in x[::-1]]).decode())([13, 88, 15]), 16) - 0 .__class__((lambda x: ''.join((chr(int.__xor__(llIIIIlllIIIlIIllI, 1)) for llIIIIlllIIIlIIllI in x)))([48, 100, 56]), 16):
        await IIlIlIlIIIIIIlllIlll.answer((lambda x: b''.__class__([IlIlIIlllIllIlllIIIlIIlIIll ^ 199 for IlIlIIlllIllIlllIIIlIIlIIll in x[::-1]]).decode())([253, 121, 23, 124, 23, 70, 22, 127, 23, 64, 22, 231, 114, 23, 121, 23, 122, 23, 69, 22, 125, 23, 114, 23, 71, 22, 71, 22, 121, 23, 125, 23, 231, 114, 23, 69, 22, 127, 23, 115, 23, 114, 23, 117, 23, 85, 23, 231, 233, 126, 23, 114, 23, 124, 23, 118, 23, 68, 22, 71, 22, 231, 247, 246, 231, 234, 231, 72, 22, 127, 23, 122, 23, 114, 23, 122, 23, 124, 23, 121, 23, 120, 23, 121, 23, 120, 23, 231, 119, 23, 123, 23, 123, 23, 68, 22, 70, 22, 231, 72, 22, 119, 23, 122, 23, 75, 22, 124, 23, 119, 23, 123, 23, 127, 23, 122, 23, 127, 23, 91, 23, 231, 72, 127, 40, 103, 93, 37]))
        return
    llIlIllllIIIll = lIllIIlIlllIIIIlIIIlIlllll[(lambda x: b''.__class__([IlIlIIlllIllIlllIIIlIIlIIll ^ 214 for IlIlIIlllIllIlllIIIlIIlIIll in x[::-1]]).decode())([162, 184, 191])](IIlIlIlIIIIIIlllIlll.text)
    IIIlllllIlIllllIlllII = llIlIllllIIIll * lllllIlIIIllIIllIlIIlI
    lIlllIIllIIlIlllI = await IIIIIlIIIIlIlIlllIllIIIlllI.get_data()
    nickname = lIlllIIllIIlIlllI[(lambda x: ''.join((chr(int.__xor__(llIIIIlllIIIlIIllI, 63)) for llIIIIlllIIIlIIllI in x)))([81, 86, 92, 84, 81, 94, 82, 90])]
    label = f"don_{IIlIlIlIIIIIIlllIlll.from_user.id}_{lIllIIlIlllIIIIlIIIlIlllll[(lambda x: ''.join((chr(int.__xor__(llIIIIlllIIIlIIllI, 60)) for llIIIIlllIIIlIIllI in x)))([85, 82, 72])](lllllIllIIII())}"
    await IIIIIlIIIIlIlIlllIllIIIlllI.update_data(amount=llIlIllllIIIll, reward=IIIlllllIlIllllIlllII, label=label)
    lIlIIIIlIIIIIIIllIlIlII = Quickpay(receiver=llIIllllIIIllIIllllIII, quickpay_form=(lambda IIllIllllIIlllII: int.__xor__(IIllIllllIIlllII, 1324096503).to_bytes(4, 'big').decode())(1032090759), targets=f'Донат для {nickname}', paymentType=(lambda IIllIllllIIlllII: int.__xor__(IIllIllllIIlllII, 4593).to_bytes(2, 'big').decode())(17075), sum=llIlIllllIIIll, label=label)
    llIllllIIlllllIIll = InlineKeyboardBuilder()
    llIllllIIlllllIIll.row(types.InlineKeyboardButton(text=(lambda x: b''.__class__([IlIlIIlllIllIlllIIIlIIlIIll ^ 27 for IlIlIIlllIllIlllIIIlIIlIIll in x[::-1]]).decode())([151, 202, 153, 202, 163, 203, 153, 202, 171, 203, 160, 203, 164, 203, 133, 203, 59, 168, 137, 132, 235]), url=lIlIIIIlIIIIIIIllIlIlII.redirected_url))
    llIllllIIlllllIIll.row(types.InlineKeyboardButton(text=(lambda IIIlIIlIIIlIIll: b''.fromhex(IIIlIIlIIIlIIll)[::-1].decode())('83d182d1b0d0bbd0bfd0bed0208cd182d1b8d080d1b5d0b2d0bed080d19fd02084949ff0'), callback_data=(lambda IIIlIIlIIIlIIll: b''.fromhex(IIIlIIlIIIlIIll)[::-1].decode())('746e656d7961705f6b63656863')))
    await IIlIlIlIIIIIIlllIlll.answer(f'📝 <b>Заявка на донат создана!</b>\n\n👤 Игрок: <code>{nickname}</code>\n💵 К оплате: <code>{llIlIllllIIIll} руб.</code>\n💎 Будет зачислено: <b>{IIIlllllIlIllllIlllII} руб. (x{lllllIlIIIllIIllIlIIlI})</b>\n\nНажмите кнопку «Оплатить», после оплаты нажмите «Проверить оплату».', parse_mode=(lambda x: ''.join((chr(int.__xor__(llIIIIlllIIIlIIllI, 21)) for llIIIIlllIIIlIIllI in x)))([93, 65, 88, 89]), reply_markup=llIllllIIlllllIIll.as_markup())

@lllIlIIIIlIlIlIlIIIIll.callback_query(F.lIlllIIllIIlIlllI == (lambda IIllIllllIIlllII: int.__xor__(IIllIllllIIlllII, 3070541763321247937318311788485).to_bytes(13, 'big').decode())(5519067934727987572427077456305))
async def lIIlIllIlIIIll(lIIIllIIlllIl: types.CallbackQuery, IIIIIlIIIIlIlIlllIllIIIlllI: FSMContext):
    lIlllIIllIIlIlllI = await IIIIIlIIIIlIlIlllIllIIIlllI.get_data()
    if (lambda x: b''.__class__([IlIlIIlllIllIlllIIIlIIlIIll ^ 22 for IlIlIIlllIllIlllIIIlIIlIIll in x[::-1]]).decode())([122, 115, 116, 119, 122]) not in lIlllIIllIIlIlllI:
        await lIIIllIIlllIl.answer((lambda x: ''.join((chr(int.__xor__(llIIIIlllIIIlIIllI, 42)) for llIIIIlllIIIlIIllI in x)))([9177, 10, 1035, 1055, 1131, 1131, 1042, 1125, 10, 1129, 1131, 1128, 1050, 1130, 1055, 1041, 1050, 4, 10, 1079, 1050, 1133, 1047, 1042, 1128, 1055, 10, 1053, 1050, 1047, 1044, 1048, 1044, 10, 1131, 10, 1040, 1044, 1046, 1050, 1047, 1054, 1121, 10, 5, 89, 94, 75, 88, 94]), show_alert=True)
        return
    label = lIlllIIllIIlIlllI[(lambda IIIlIIlIIIlIIll: b''.fromhex(IIIlIIlIIIlIIll)[::-1].decode())('6c6562616c')]
    IIIlllllIlIllllIlllII = lIlllIIllIIlIlllI[(lambda x: b''.__class__([IlIlIIlllIllIlllIIIlIIlIIll ^ 103 for IlIlIIlllIllIlllIIIlIIlIIll in x[::-1]]).decode())([3, 21, 6, 16, 2, 21])]
    nickname = lIlllIIllIIlIlllI[(lambda IlIIlIIIIlII: bytes([int.__xor__(int(IlIIlIIIIlII[IlIlIIlllIllIlllIIIlIIlIIll:IlIlIIlllIllIlllIIIlIIlIIll + 2], 16), 91) for IlIlIIlllIllIlllIIIlIIlIIll in range(0, len(IlIIlIIIIlII), 2)]).decode())('35323830353a363e')]
    try:
        llIIIlIIIIlIllllll = Client(IllIlIIlllIllIllllIllIlIllI)
        IllIlIlllIlIlIlIlIlllll = llIIIlIIIIlIllllll.operation_history(label=label)
        IIllllIlIIlIlIlIIIIIlII = False
        for IllllIIIIIIlllI in IllIlIlllIlIlIlIlIlllll.operations:
            if IllllIIIIIIlllI.status == (lambda IIllIllllIIlllII: int.__xor__(IIllIllllIIlllII, 45388982552905994).to_bytes(7, 'big').decode())(59167372408076921):
                IIllllIlIIlIlIlIIIIIlII = True
                break
        if IIllllIlIIlIlIlIIIIIlII:
            success = llIIlIlIlIllII(nickname, IIIlllllIlIllllIlllII)
            if success:
                await lIIIllIIlllIl.IIlIlIlIIIIIIlllIlll.edit_text(f'✅ <b>Оплата успешно подтверждена!</b>\n\nНа аккаунт <code>{nickname}</code> зачислено <b>{IIIlllllIlIllllIlllII} руб.</b>\nДонат появится в игре в ближайшее время. Приятной игры!', parse_mode=(lambda IlIIlIIIIlII: bytes([int.__xor__(int(IlIIlIIIIlII[IlIlIIlllIllIlllIIIlIIlIIll:IlIlIIlllIllIlllIIIlIIlIIll + 2], 16), 62) for IlIlIIlllIllIlllIIIlIIlIIll in range(0, len(IlIIlIIIIlII), 2)]).decode())('766a7372'))
                await IIIIIlIIIIlIlIlllIllIIIlllI.clear()
            else:
                await lIIIllIIlllIl.answer((lambda x: ''.join((chr(int.__xor__(llIIIIlllIIIlIIllI, 73)) for llIIIIlllIIIlIIllI in x)))([9989, 105, 1111, 1025, 1137, 1144, 1139, 1145, 105, 1150, 1145, 1142, 1137, 1032, 1137, 105, 1147, 105, 1112, 1117, 103, 105, 1128, 1147, 1030, 1151, 1137, 1035, 1148, 1032, 1029, 105, 1032, 105, 1145, 1149, 1141, 1137, 1140, 1137, 1032, 1035, 1033, 1145, 1039, 1137, 1148, 1136, 103]), show_alert=True)
        else:
            await lIIIllIIlllIl.answer((lambda x: ''.join((chr(int.__xor__(llIIIIlllIIIlIIllI, 57)) for llIIIIlllIIIlIIllI in x)))([10101, 25, 1062, 1026, 1033, 1147, 1036, 1039, 25, 1028, 1036, 25, 1028, 1033, 1024, 1037, 1036, 1028, 23, 25, 1068, 1144, 1026, 1025, 25, 1035, 1138, 25, 1031, 1030, 1026, 1033, 1147, 1025, 1026, 1025, 21, 25, 1030, 1031, 1037, 1031, 1039, 1037, 1025, 1147, 1036, 25, 8, 25, 1029, 1025, 1028, 1146, 1147, 1146, 23]), show_alert=True)
    except Exception as llIIllllIIIIIlIIIll:
        IIllIIIllIIllIIlIlIlllIIlll(f'YooMoney Error: {llIIllllIIIIIlIIIll}')
        await lIIIllIIlllIl.answer((lambda IlIIlIIIIlII: bytes([int.__xor__(int(IlIIlIIIIlII[IlIlIIlllIllIlllIIIlIIlIIll:IlIlIIlllIllIlllIIIlIIlIIll + 2], 16), 209) for IlIlIIlllIllIlllIIIlIIlIIll in range(0, len(IlIIlIIIIlII), 2)]).decode())('334b713e695ef1014f005901690160016b0161f10050016400510163016400510161f1016f016e016a01610053005afff1014e016f016e0051016f01600052016800530164f1016e016f016601670164ff'), show_alert=True)

async def llIIllIllIIIllllllllllIllII():
    lIllIIlIlllIIIIlIIIlIlllll[(lambda x: ''.join((chr(int.__xor__(llIIIIlllIIIlIIllI, 16)) for llIIIIlllIIIlIIllI in x)))([96, 98, 121, 126, 100])](f'Бот запущен! Множитель доната: x{lllllIlIIIllIIllIlIIlI}')
    await lllIlIIIIlIlIlIlIIIIll.start_polling(IllllllIIlllI)
if __name__ == (lambda IIIlIIlIIIlIIll: b''.fromhex(IIIlIIlIIIlIIll)[::-1].decode())('5f5f6e69616d5f5f'):
    lllIIIlIllIIIIllllll(llIIllIllIIIllllllllllIllII())
