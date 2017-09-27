class Demo:
    axiom = 'F'
    rules = {
        'F': 'FF[f]-',
        'f': '+F'
    }
    angle = 20

class Fibonacci:
    axiom = 'A'
    rules = {
        'A': 'AB',
        'B': 'A'
    }


class KochIsland:
    axiom = 'F-F-F-F'
    rules = {
        'F': 'F-F+F+FF-F-F+F'
    }

class QuadraticSnowflake:
    axiom = '-F'
    rules = {
        'F': 'F+F-F-F+F'
    }

class IslandsAndLakes:
    axiom = 'F+F+F+F'
    rules = {
        'F': 'F+f-FF+F+FF+Ff+FF-f+FF-F-FF-Ff-FFF',
        'f': 'ffffff'
    }

class Plant:
    axiom = 'X'
    rules = {
        'X': 'F-[[X]+X]+F[+FX]-X',
        'F': 'FF'
    }
    angle = 22.5

class Penrose:
    axiom = '[N]++[N]++[N]++[N]++[N]'
    rules = {
        'M': 'OA++PA----NA[-OA----MA]++',
        'N': '+OA--PA[---MA--NA]+',
        'O': '-MA++NA[+++OA++PA]-',
        'P': '--OA++++MA[+PA++++NA]--NA',
        'A': ''
    }
    angle = 36

class Arrowhead:
    axiom = 'A'
    rules = {
        'A': 'B-A-B',
        'B': 'A+B+A'
    }
    angle = 60

class DragonCurve:
    axiom = 'FX'
    rules = {
        'X': 'X+YF+',
        'Y': '-FX-Y'
    }

class Triangle:
    axiom = 'W'
    rules = {
        'W': '+++X--F--ZFX+',
        'X': '---W++F++YFW-',
        'Y': '+ZFX--F--Z+++',
        'Z': '-YFW++F++Y---',
    }
    angle = 30
    n = 6

class Stress:
    axiom = 'XmnckzHIqSsRGtzTceAJiGGHIBKcfZQiwsCoDAMEQvmmWbrpQXbgKFgVMnYRyXxNGEmmGLxTKaJzVfkrFSVuZsMDtjRuSqrLYKUk'
    rules = {
	'A': 'BxCSlCiefBxyllFNoxn+IKkiWTnUwlWVIYHBXgV+fBda]eFe-io[snRJQdqDAHyjaRtAHfDhmJIWystiurgNFotRlRpGmyFDxPve',
	'C': 'hEblAfJ[WHTnlaNhTxDo]O-cGZpBZ+VHZtgLTzSBWMzQwwpNU-CFDNDV]z+Rqolk-GGkilHDDGHRUzczzGs-cwDwXjPmJXjetBiy',
	'B': 'HdgdOPzlbzjZrY+ApwBo[tA-V[TpEljDbxLWQxmy[IeNdyQsdUxflfbjJHjKCkLxFliuBulyE-orSepLVSPaDLqCvLdvEfAh[nAZ',
	'E': 'qkBGCCTOcocZbDQg]]sQEs-OEsJyeEeTEmlaKKdW[ZcBYMXeBALQVKbYime[hBPdYcrLVXpflySABREqkpaUlIypjr-twuDQsZeA',
	'D': 'qhQTanqhznUMpI[oGsxzJbeVdpZeDPzDqTy+tgmysd[egrDIbr[Q+MzUrK+AdbjZGDEebECPhPBwSyueaNWoFBmZUmNOLtaMXU+u',
	'G': 'KGYcJWRaGITUGipbVwDPvgnBK+dGrhBTfB[MxUAoExtpohYD+DHFTUbECcAf-sKN+JLTOIomwsnmPFANOsJDemQcYgAvxl-QUuF[',
	'F': 'Tz++VX-MeItPeZ[GOgkA[dZAdMNVvkcmRhjWsNa+ElVSvnYlNefQJhKuG+LaqncU]DreKYRrGLSpbewnMXHMfHIn+iGQsVNOzp+q',
	'I': 'gjZX[vpjmVuxw-uyMZnEj-tQTDPRDtDuuBEqcIndyDHrM[LshUrlYrXWdbnxRLByeWjNAzsJlaSOBhseIrq[bVCzWoqONHDrscIU',
	'H': 'xKuxvqfYFhUW]HyFEvGEYEteQoxwBwWnPi]knFJSLfZtyh]tjwUUb]YhPmoLjOPqZVgw-oyomU[OITOdCHBaSvUHFoTOrIhNwNGa',
	'K': 'b+SpBVJPupmKKuFU]BJNaTZRJrtBbvZ[IOKZGwsWtyYNL+DyTUTEwsMhJyFXtcYfgWtsB-[MurhTdu]r-RvNocqMVSJBRhgTQXmr',
	'J': 'C]PXrzvaiiQBouHOASHQTgTUWILIGZRwqDkylERsn-hVqHriS[oUdCTLVOddtqxVKlVOYAMNyeLljTsNGHJs-I+iYVPYBoF++hcw',
	'L': 'f-NT[DuRjITpaZrjEIWrVUPYHwLxv[AsDz-OPXSfzMaTpJqwq+ZSevutdmcWnRINEFpFKQGSmIGASMEsLmAtvLG]Cl-IBKnwLEbt',
	'O': 'DuLSbwuiEVTarWTpwPoeVAKHUciPAcmglMBcMryH[IrZptzpO+]UIv[nDb-[+ieZdok-iYvesyaBQwrsTltjh[QxhkbQHG+xjjpb',
	'N': 'sfIlOtYhSFMcDVJqFVUuWervUSmCpPKgCsCEJkBeqOVJ-OvJbtDYrLheGb-wHqSO-ZDY-XSN[rinHSfogLfDKJheVeqLPRxhJFEv',
	'Q': 'aslpRqwZkkujMWBKizkzduckLrAEj]PHbVHhnunZmls]BD-cRrQrU[GhXE-ygldgdwtoM[Bo+pzQUyCIIGqrPIVkhSIpFJtrXyuX',
	'P': 'CdnNGIsQOkNJxsJEXRtKLrwEXCkl[-tzTXRBXqu+pVatZb+WblTcUjYNtgeujklyApHrCfNOvufihuaQ-out[Za[q-RnAgmjGDy-',
	'S': 'jQrOl][MDpXwIZYMAzulXfigz[T-SFdMLXpITFMWCOQlmE]toofGFehGBuBThj]XA]JyTofVjyy]JYbSALvtGzWKlrrCCJlNK[vb',
	'R': '-+ENvtLSFT+YuBaLDPKhPbEabGCnBkhckbLEqPgvLCiX[SWYZbDeuNqOLojmKNloMGTW+elli]Q]mzNaRafi]Sm[FLtuyWAqYRZk',
	'U': 'krWssAMql]Xz]bQXgQqNS]HhtTc[lRXgpUNlpmbXHqL--j[wnvNSlhrVrLOQLUkEMRUwjddYaRdaQvcqNbPnRC+XiJmLgJAn[i]f',
	'T': 'ymjuWvYmVhMraVeZsFJLYNSK-sFgUZztm-JtBhvfGuFrdTEyrWacCbcmliMVSi[SJtKfswH+wgDCYFspNfaNWTqhbVMvOedPb-Tn',
	'W': 'pzgSdhhmvCygGfKBXmMcwoynxOTJNqdRV+UlfkODabIfUIwxOayH[lDVxnJYkulPfUAUvLq[XmJwbHSV[]NpTbcyKqJieF-PvUxV',
	'V': 'RSDtIuMj+YRvwcD]RBMHGXdZyS[lKWXbqTDRSmGPwOuWOAwqdqamMxfhSK]yXuyKJjeZ+ZntlXbprwybDiO-EVprTVdBWrKrE[mo',
	'Y': 'iTkNUkHtyJNpYeSPVGKXIaOyujkxcDeJk[lBTW[tjv[pHynhsmlCfxDsiTYU[w]Up]LozWeXKXSqNuDCjhpxX]+iDcTFQtxMXZsM',
	'X': 'MAZiqJAjfqVZTkF-IWuFBpydTtNTAX-TCAjLsZig]YYJog+]hR-xW]xfZaGxzgroOEBVMUTeCmspcmdjjMS[J+l-UXNt-gSTh]uO',
	'Z': 'lepDjvLISiOnpqGIbvprXIzp[MXgRGLJAUuTutXFAVcCUqqDgPKoWXbjbophpxfBhsZfvFQW[biGpIQlFyYjKxmfm]nTouMjWhMb',
	'a': 'YKpqPjZgBSiMjGhbeJuuVNV[hJ-iDBXp-LkoZBHKUNijUDboelLvqFxkeQsLlnyGOSVxwmRKjmVuXgZyzrCCxllAtNGhcLKfZhWC',
	'c': 'ZgFywWLFZyJ-KSnauqHCsQntiZipsJitteRpJQEFourrjEGTCMjwSyYm-cgrLJXSZTROAmkCQTUKsAaoxWquVutZMQmWkflwXxtb',
	'b': 'qypqyjPnX+fRWY+FJVFGyCTd]ZcSdfOjLIRN-QXZVfTa-HMNecWDj-FTBOJHzuUedqKxbrYatWAJ]hiH]GxfKsUjzKZNjPEYLVCL',
	'e': 'ostkhYZz[ALDNJbSPCuWXLJSRmJ[pQiN-OhwcewYivpqjbvGeXAQkEvcXpRXUwMjt+tJBnrWiGKHbJq[nGNOQHiVyOaaotysUgyx',
	'd': 'aaXUK-PrpDVK]bcbmJm-wVUAfxFntCVszwfbBXQ+JkyfUXjYgmI[v-VpCKLuaSL[uUeDMyFCeWO+YUpNuMadXTjQvOvipNJywiJR',
	'g': 'MMPRbdI[lHmBjzFxSQXrxhPBfPKeuX+GRvFgSpZhEfHfKxtzBjhnoHPEJClVzWA]MfvkSfZmE-aEDSpKiMzV[wZPuEwlUPXbTqOA',
	'f': 'AVAxo[TNwSazURg]cxgWWjWKwEyAAveFDBgSeHhcvfCJOhtBnVqTVVPSSVgLs]fvqW]OMlCoBpjwJTSdibIeahqpSyuiaKjQGJb[',
	'i': 'GCHJg]SRGduomb]KEPZl[LhjoXkjAExHE[dddJppUstrNLgwRccdNrWX[WhpM+iPFQvmxnjqWUiSVMdICusVbBBAqOflvwewUSxh',
	'h': 'vEr]JlQlzIkXziwB-zHZ-]NJQMiMzdwvdpskBwlIk+ToidMneJEZzvtpx+MZKKYOJYNshO]DdhxxubMQHw[W+tjljQJDvkjOumz[',
	'k': 'HYIwSQINiDxrTqcFhFhrMI+]vxaNTk+AROrHTSQgtGjEZPiwGmY+NvE[Xy+HxlJrms[MsByIE[zRvlMbZ-jmvCvCITMgjTyYqWSG',
	'j': 'daqMUx]M[NkNNqle-bjfLghDEydTaqEMyRBFEsAgGxDewwiVlnqlbvFY-klbDQLAlpwStsDSbj+EsAFRRvu+LkNJfkgNriUrnaVh',
	'm': 'Dzwpm+kzRPvkANBqAgrQAenrBUxGSpIRAiJywmlpaNLZDrqlVOJHISJSjRajowTT]wCVpVHFOCmSlxxf-WgAtXhgrPvd+MJuqWXz',
	'l': 'MTKbSNHMGFbuOEIHVcuLFlIlxUrbN-ESevqOoATlFUV-IyCsjR-TULSd+rAt-wspVxzifbNX-lMUgPKiZsDAWfuvBVEq-ijZpG[y',
	'o': 'CL]yhOtJbaAcpIAIoLYWf]PedAZfmZ[CVlrKfco-fxhg[QnCPOmECNHpLklOx+MePytPSEymfGeobWXiVVZb]aeFa+]JtMdteoHG',
	'n': 'WTOnUvCwiDWdSiEZnOhsgHoABTpPLvFJmytnjYjBMEUzorZV-cUxRwhHfiAY[EyuUJSdwHxURWuyacHRMcCbBFbvUsovTcHQQ+xH',
	'q': 'zMWTB[uGsYWVLgvFQsZBVVXTFmiIzsRHHf+hEYXjgNIJEzmmXdVGByoqsChyTcT+KrSpxanMIUwjgwSl]wljHRRZQwwhmBcmDWeS',
	'p': 'NTi[QHg[HqhWPShmcVgaaXqYyXzEresbKOqNoKyMzDB[OkTMdkacIsWWymvyFFx]gwYaeEQRGaVQbVlLvguVQ[kwDDQPyzCRUFYL',
	's': 'NaPTTugtYffwLhLjbqCf-FcsZEytAvq]GrTFqYuBkzwEqXOaBxKb+SiUXYKiGgylMsXZRVzPkeGEVv]UoH+]sVcMPK[rfnCDLX]E',
	'r': '[CqpLIlOpMuzzbUuFAVSupaWkovNhDJdqeicGznbvE-W+URTCBiKCeFKxDlqwTZUSCxOBgdljYd[ZsIpYYOodJ[G]dqB+rfhOkIg',
	'u': 'EWBXAuOUBpPXLvsXcqtbucU[FwMZfGqLhiTHCUfjfKHbGWbLopGzAfwoMREhBZTnPpYchzLJHUyZpbTtlQxIqPYtUJeogRMKuCHX',
	't': 'GRWd]LztLPTDnlWLXSM[FGhFBPGkWGGKJzljsfVOqo-JCZnEiHgxZMZHhGmlEwSotMZqZ[bXc+T]SGJmSEOAEYQyFSOwVvaCSkqA',
	'w': '+-TIbRmWpUUNxMNFpiDfXmYMXOlK+OSfcDUpgdqNxoPr]Ap]M-LSCHLuwiT[YBrJAVxYeZSgiMKQEjiVzBAtGNQ+oln-BOlz-VcO',
	'v': 'elixArIyfpjeUIEUUEkBGZSyayZiZoZBpjglLgQydOIjhMFuKHy[hGQsTsJpfXEI[-vXamxsLEDNTSeJpBczpcfUeFOoTwFQ-mWs',
	'y': 'Zy]BQcQnEZrdEEispriwUgsDJszDRrG+XlytYYFQlnaBRyWN[jgCqs]ZLtNYopBqwWDCCgtZGqgytOOwcqrazw[Ae[K]UyFMPDCI',
	'x': 'BssydTunukLDtlXRF+VIqHEoYUuqnTrhrZzxJIeq+VlTb][VpL-OrMUeVALZVzYcobmwlVoyAAbF]GyMQeBE]XDXvZEgizuugYIy',
	'z': 'inNpgJdTppVNUUndfuOjJQmrsTSO[hmSQv-rWXrvZ]pjPKdxBdAn+FCkFlih+NGBvKzUz-+P-zcR-BAAomACFmeezH+Dnzp-jEOz',
    }
