from pyobigram.utils import sizeof_fmt,nice_time
import datetime
import time
import os

def text_progres(index,max):
	try:
		if max<1:
			max += 1
		porcent = index / max
		porcent *= 100
		porcent = round(porcent)
		make_text = ''
		index_make = 1
		make_text += '\n['
		while(index_make<21):
			if porcent >= index_make * 5: make_text+='●'
			else: make_text+='○'
			index_make+=1
		make_text += ']\n'
		return make_text
	except Exception as ex:
			return ''

def porcent(index,max):
    porcent = index / max
    porcent *= 100
    porcent = round(porcent)
    return porcent

def createDownloading(filename,totalBits,currentBits,speed,time,tid=''):
    msg = '<i class="fas fa-angle-double-down"></i>Descargando... \n\n'
    msg+= '📌Nombre: ' + str(filename)+'\n'
    msg+= '🗃️Tamaño Total: ' + str(sizeof_fmt(totalBits))+'\n'
    msg+= '📩Descargado: ' + str(sizeof_fmt(currentBits))+'\n'
    msg+= '🛰️Velocidad: ' + str(sizeof_fmt(speed))+'/s\n'
    msg+= '⏳Tiempo: ' + str(datetime.timedelta(seconds=int(time))) +'\n\n'

    msg = '📤 𝔻𝕖𝕤𝕔𝕒𝕣𝕘𝕒𝕟𝕕𝕠 𝕖𝕤𝕡𝕖𝕣𝕖....\n\n'
    msg += '🎟️ 𝔸𝕣𝕔𝕙𝕚𝕧𝕠: '+filename+'\n'
    msg += text_progres(currentBits,totalBits)+'\n'
    msg += '🎰 Porcentaje: '+str(porcent(currentBits,totalBits))+'%\n\n'
    msg += '🎫 Total: '+sizeof_fmt(totalBits)+'\n\n'
    msg += '📩 Descargado: '+sizeof_fmt(currentBits)+'\n\n'
    msg += '🛰️ Velocidad: '+sizeof_fmt(speed)+'/s\n\n'
    msg += '⏳ Tiempo de Descarga: '+str(datetime.timedelta(seconds=int(time)))+'s\n\n'

    if tid!='':
        msg+= '/cancel_' + tid
    return msg
def createUploading(filename,totalBits,currentBits,speed,time,originalname=''):
    msg = '📤 𝕊𝕦𝕓𝕚𝕖𝕟𝕕𝕠 𝕒 𝕝𝕒 𝕟𝕦𝕓𝕖☁... \n\n'
    msg+= '🎭 ℕ𝕠𝕞𝕓𝕣𝕖: ' + str(filename)+'\n'
    if originalname!='':
        msg = str(msg).replace(filename,originalname)
        msg+= '📤 𝕊𝕦𝕓𝕚𝕖𝕟𝕕𝕠: ' + str(filename)+'\n'
    msg+= '🗂 𝕋𝕒𝕞𝕒𝕟̃𝕠 𝕥𝕠𝕥𝕒𝕝: ' + str(sizeof_fmt(totalBits))+'\n'
    msg+= '🗂 𝕊𝕦𝕓𝕚𝕕𝕠: ' + str(sizeof_fmt(currentBits))+'\n'
    msg+= '📶 𝕍𝕖𝕝𝕠𝕔𝕚𝕕𝕒𝕕: ' + str(sizeof_fmt(speed))+'/s\n'
    msg+= '🕐 𝕋𝕚𝕖𝕞𝕡𝕠: ' + str(datetime.timedelta(seconds=int(time))) +'\n'

    msg = '⏫  𝕊𝕦𝕓𝕚𝕖𝕟𝕕𝕠 𝕒 𝕝𝕒 𝕟𝕦𝕓𝕖☁...\n\n'
    msg += '🔖 ℕ𝕠𝕞𝕓𝕣𝕖: '+filename+'\n'
    if originalname!='':
        msg = str(msg).replace(filename,originalname)
        msg+= '🔖 ℙ𝕒𝕣𝕥𝕖: ' + str(filename)+'\n'
    msg += text_progres(currentBits,totalBits)+'\n'
    msg += '📊 ℙ𝕠𝕣𝕔𝕖𝕟𝕥𝕒𝕘𝕖: '+str(porcent(currentBits,totalBits))+'%\n\n'
    msg += '🗂 𝕋𝕠𝕥𝕒𝕝: '+sizeof_fmt(totalBits)+'\n\n'
    msg += '🗂 𝔻𝕖𝕤𝕔𝕒𝕣𝕘𝕒𝕟𝕕𝕠: '+sizeof_fmt(currentBits)+'\n\n'
    msg += '📶 𝕍𝕖𝕝𝕠𝕔𝕚𝕕𝕒𝕕: '+sizeof_fmt(speed)+'/s\n\n'
    msg += '🕐 𝕋𝕚𝕖𝕞𝕡𝕠 𝕕𝕖 𝕕𝕖𝕤𝕔𝕒𝕣𝕘𝕒: '+str(datetime.timedelta(seconds=int(time)))+'s\n\n'

    return msg
def createCompresing(filename,filesize,splitsize):
    msg = '📚ℂ𝕠𝕞𝕡𝕣𝕚𝕞𝕚𝕖𝕟𝕕𝕠... \n\n'
    msg+= '🔖ℕ𝕠𝕞𝕓𝕣𝕖: ' + str(filename)+'\n'
    msg+= '🗂𝕋𝕒𝕞𝕒𝕟̃𝕠 𝕥𝕠𝕥𝕒𝕝: ' + str(sizeof_fmt(filesize))+'\n'
    msg+= '📂𝕋𝕒𝕞𝕒𝕟̃𝕠 𝕣𝕟 𝕡𝕒𝕣𝕥𝕖𝕤: ' + str(sizeof_fmt(splitsize))+'\n'
    msg+= '💾ℂ𝕒𝕟𝕥𝕚𝕕𝕒𝕕 𝕕𝕖 𝕡𝕒𝕣𝕥𝕖𝕤: ' + str(round(int(filesize/splitsize)+1,1))+'\n\n'
    return msg
def createFinishUploading(filename,filesize,split_size,current,count,findex):
    msg = '📌ℙ𝕣𝕠𝕔𝕖𝕤𝕠 𝕗𝕚𝕟𝕒𝕝𝕚𝕫𝕒𝕕𝕠📌\n\n'
    msg+= '🔖ℕ𝕠𝕞𝕓𝕣𝕖: ' + str(filename)+'\n'
    msg+= '🗂𝕋𝕒𝕞𝕒𝕟̃𝕠 𝕥𝕠𝕥𝕒𝕝: ' + str(sizeof_fmt(filesize))+'\n'
    msg+= '📂𝕋𝕒𝕞𝕒𝕟̃𝕠 𝕕𝕖𝕓𝕝𝕒𝕤 𝕡𝕒𝕣𝕥𝕖𝕤: ' + str(sizeof_fmt(split_size))+'\n'
    msg+= '📤ℙ𝕒𝕣𝕥𝕖𝕤 𝕤𝕦𝕓𝕚𝕕𝕒𝕤: ' + str(current) + '/' + str(count) +'\n\n'
    msg+= '🗑𝔹𝕠𝕣𝕒𝕣 𝕒𝕣𝕔𝕙𝕚𝕧𝕠: ' + '/del_'+str(findex)
    return msg

def createFileMsg(filename,files):
    import urllib
    if len(files)>0:
        msg= '<b>🖇𝔼𝕟𝕝𝕒𝕔𝕖🖇</b>\n'
        for f in files:
            url = urllib.parse.unquote(f['directurl'],encoding='utf-8', errors='replace')
            #msg+= '<a href="'+f['url']+'">🔗' + f['name'] + '🔗</a>'
            msg+= "<a href='"+url+"'>🔗"+f['name']+'🔗</a>\n'
        return msg
    return ''

def createFilesMsg(evfiles):
    msg = '📑𝔸𝕣𝕔𝕙𝕚𝕧𝕠𝕤 ('+str(len(evfiles))+')📑\n\n'
    i = 0
    for f in evfiles:
            try:
                fextarray = str(f['files'][0]['name']).split('.')
                fext = ''
                if len(fextarray)>=3:
                    fext = '.'+fextarray[-2]
                else:
                    fext = '.'+fextarray[-1]
                fname = f['name'] + fext
                msg+= '/txt_'+ str(i) + ' /del_'+ str(i) + '\n' + fname +'\n\n'
                i+=1
            except:pass
    return msg
def createStat(username,userdata,isadmin):
    from pyobigram.utils import sizeof_fmt
    msg = '⚙️Configuraciones De Usuario⚙️\n\n'
    msg+= '🔖𝐍𝐨𝐦𝐛𝐫𝐞: @' + str(username)+'\n'
    msg+= '👤 𝐔𝐬𝐮𝐚𝐫𝐢𝐨: ' + str(userdata['moodle_user'])+'\n'
    msg+= '🔑𝐂𝐨𝐧𝐭𝐫𝐚𝐬𝐞𝐧̃𝐚: ' + str(userdata['moodle_password']) +'\n'
    msg+= '📡𝐍𝐮𝐛𝐞: ' + str(userdata['moodle_host'])+'\n'
    if userdata['cloudtype'] == 'moodle':
        msg+= '🏷𝐑𝐞𝐩𝐨𝐈𝐃: ' + str(userdata['moodle_repo_id'])+'\n'
    msg+= '🏷𝐂𝐥𝐨𝐮𝐝𝐭𝐲𝐩𝐞: ' + str(userdata['cloudtype'])+'\n'
    msg+= '📟𝐔𝐩𝐭𝐲𝐩𝐞: ' + str(userdata['uploadtype'])+'\n'
    if userdata['cloudtype'] == 'cloud':
        msg+= '🗂𝐃𝐢𝐫: /' + str(userdata['dir'])+'\n'
    msg+= '📚𝐓𝐚𝐦𝐚𝐧̃𝐨 𝐝𝐞 𝐳𝐢𝐩𝐬 : ' + sizeof_fmt(userdata['zips']*1024*1024) + '\n\n'
    msgAdmin = '🚫'
    if isadmin:
        msgAdmin = '✅'
    msg+= '🛡️ 𝐎𝐖𝐍𝐄𝐑: ' + msgAdmin + '\n'
    proxy = '😓'
    if userdata['proxy'] !='':
       proxy = '✅'
    rename = '🚫'
    if userdata['rename'] == 1:
       rename = '✅'
    msg+= '📝𝐑𝐞𝐧𝐚𝐦𝐞 : ' + rename + '\n'
    msg+= '🔌𝐏𝐫𝐨𝐱𝐲 : ' + proxy + '\n\n'
    msg+= '⚙️𝐍𝐮𝐛𝐞𝐬 𝐜𝐨𝐧𝐟𝐢𝐠⚙️: \n'
    msg+= '𝐄𝐯𝐚: /seteva\n'
    msg+= '𝐂𝐮𝐫𝐬𝐨𝐬: /setcursos\n'
    msg+= '𝐄𝐝𝐮: /setedu\n'
    msg+= '𝐔𝐜𝐥𝐯: /setuclv\n'
    msg+= '𝐄𝐯𝐞𝐚: /setevea\n'
    msg+= '𝐒𝐥𝐝: /setsld\n'
    msg+= '𝐆𝐭𝐦: /setgtm\n'
    msg+= '𝐔𝐯𝐬: /setuvs\n'
    msg+= '𝑽𝒄𝒍: /setvcl\n'
    return msg
