# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

a = 'ABRDACKOAFKSAFLTAGROAKRNALRSAMEZAPTKAQUAARSAASSBAVANBANEBANEPBELUBISVPBLNGBRZLBSPBBSPBPCBOMCHGZCHKZCHMFCHMKCIANCNTLCNTLPDIODDSKYDVECDZRDDZRDPEELTELFVELTZENPGETLNFEESFESHFIVEFIXPFLOTGAZAGAZAPGAZCGAZPGAZSGAZTGCHEGECOGEMAGEMCGLTRGMKNGTRKHHRUHIMCPHMSGHYDRIGSTIGSTPINGRIRAOIRKTISKJJNOSJNOSPKAZTKAZTPKBSBKCHEKCHEPKGKCKGKCPKLSBKMAZKMEZKMTZKOGKKRKNKRKNPKRKOPKROTKROTPKRSBKRSBPKTSBKTSBPKUBEKUZBKZOSKZOSPLENTLIFELKOHLNZLLNZLPLPSBLSNGLSNGPLSRGLVHKMAGEMAGEPMAGNMDMGMFGSMFGSPMGNTMGNZMGTSMGTSPMISBMISBPMOEXMRKCMRKKMRKPMRKSMRKUMRKVMRKYMRKZMRSBMSNGMSRSMSTTMTLRMTLRPMTSSMVIDNAUKNFAZNKHPNKNCNKNCPNKSHNLMKNMTPNNSBNNSBPNSVZNVTKOGKBOKEYOMZZPOZONPAZAPHORPIKKPLZLPMSBPMSBPPOLYPOSIPRMBQIWIRASPRBCMRDRBRENIRGSSRKKERNFTROLOROSBROSNROSTRTGZRTKMRTKMPRTSBRTSBPRUALRUSIRZSBSAGOSAGOPSARESAREPSBERSBERPSELGSFINSFTLSGZHSIBNSLENSMLTSNGSSNGSPSPBESTSBSTSBPSVAVSVETTASBTASBPTATNTATNPTCSGTGKATGKBTGKBPTGKNTNSETORSTORSPTRMKTRNFPTTLKTUZAUCSSUKUZUNACUNKLUPROURKZUSBNUTARVEONRXVGSBVGSBPVJGZVJGZPVKCOVLHZVRSBVRSBPVSMOVSYDVSYDPVTBRWTCMWTCMPWUSHYAKGYKENYKENPYNDXYRSBYRSBPZILLZVEZ'

b = ''

ind = 0

for i in a:
    if i not in b:
        b += i
        ind += 1

c = list(b)
c.sort()

print(c, ind)
    