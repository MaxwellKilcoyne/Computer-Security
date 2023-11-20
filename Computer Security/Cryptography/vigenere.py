#!/usr/bin/python3

import sys
from collections import Counter
import math

#taken from Wikipedia
letter_freqs = {
    'A': 0.08167,
    'B': 0.01492,
    'C': 0.02782,
    'D': 0.04253,
    'E': 0.12702,
    'F': 0.02228,
    'G': 0.02015,
    'H': 0.06094,
    'I': 0.06966,
    'J': 0.00153,
    'K': 0.00772,
    'L': 0.04025,
    'M': 0.02406,
    'N': 0.06749,
    'O': 0.07507,
    'P': 0.01929,
    'Q': 0.00095,
    'R': 0.05987,
    'S': 0.06327,
    'T': 0.09056,
    'U': 0.02758,
    'V': 0.00978,
    'W': 0.02361,
    'X': 0.00150,
    'Y': 0.01974,
    'Z': 0.00074
}

alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def roll(arr, shift, shiftFrom=None):
    if shiftFrom is None:
        arr = arr[::-1] if shift > 0 else arr
        shift = abs(shift) % len(arr)
        return arr[shift:] + arr[:shift]

    sizeShift = len(arr[sizeShift])
    shift = shift % sizeShift
    
    if shift == 0:
        return arr

    shiftArr = [slice(None)] * len(arr)

    if shift > 0:
        shiftArr[shiftFrom] = slice(shift, None)
    else:
        shiftArr[shiftFrom] = slice(None, shift)

    rolledArr = []
    for i in range(len(arr)):
        rolledArr.append(arr[i][tuple(shiftArr[i])])

    return rolledArr




def norm(arr):
    if len(arr) == 0:
        return 0
    
    squareSum = sum(elements ** 2 for elements in arr)
    norm = math.sqrt(squareSum)
    return norm

def subtract(arr1, arr2):
    if len(arr1) != len(arr2):
        raise ValueError("different lengths")
    else:
        finalArr = []
        for i in range(len(arr1)):
            finalArr.append(arr1[i] - arr2[i])

    return finalArr



def bestShiftTest(freq):
    actFreq = (list(letter_freqs.values()))
    sliceFreq = (list(freq.values()))
    freqDiffShift = []
    for i in range(26):
        rolledFreq = roll(sliceFreq,-i)
        freqDiff = subtract(actFreq, rolledFreq)
        freqDiffNorm = norm(freqDiff)
        freqDiffShift.append(freqDiffNorm)
    return freqDiffShift.index(min(freqDiffShift))



def pop_var(s):
    """Calculate the population variance of letter frequencies in given string."""
    freqs = Counter(s)
    mean = sum(float(v)/len(s) for v in freqs.values())/len(freqs)  
    return sum((float(freqs[c])/len(s)-mean)**2 for c in freqs)/len(freqs)

# def bestShift(freq):
#     actFreq = np.array(list(letter_freqs.values()))
#     sliceFreq = np.array(list(freq.values()))
#     freqDiffShift = []
#     for i in range(26):
#         rolledFreq = np.roll(sliceFreq,-i)
#         freqDiff = np.subtract(actFreq, rolledFreq)
#         freqDiffNorm = np.linalg.norm(freqDiff)
#         freqDiffShift.append(freqDiffNorm)
#     return freqDiffShift.index(min(freqDiffShift))

def letterFreq(str):
    letters = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z',]
    letterCounter = [0] * 26
    freq = dict(zip(letters,letterCounter))
    for char in str:
        freq[char] += 1
    for letter in freq:
        freq[letter] /= len(str)
    return freq
    
def value2Letter(num):
    return alphabet[num]

if __name__ == "__main__":
    # Read ciphertext from stdin
    # Ignore line breaks and spaces, convert to all upper case
    # cipher = sys.stdin.read().replace("\n", "").replace(" ", "").upper()
    # cipher = "TVQCEDYSLJPGXGXIJEJOPJQGPCNZWWHOJDKJIZWPQUMIGKQWNFVVWPCYSLFCTBMZVQMFLWBPNBFKLLMEAKPCQBNAJKKJLGWNYMPPVUKXRMMSIEOFJUHAVRYAMEQUOLNVGPGNYWSSWTDFJLNGJKBMIELNIATURIPNUMMAQTKLYWNTQYNMWYMCXBQWBSGNMZBVACGFNUFBCXBNVTTKUCXQYDGBMSKRJGPMWMHXVYRMMZQFVCLQAKTOCUQAOXKNTCEGQEBTKGWTDMUWGPGWMWVVVIDMDWHAKBAWQRLUSJAMEJTYYIIJIMOYSLOMCWGSOJQVRETWQVCDSWMVVCWMRMABDBGLPGIPNCFZYGVYZJAHZGKLIQGAVRCJIETALGWLNAVRCXILQPQETMFBJKRLMGAVRCWIGQQXQLMBZIOQMIXMWZWTCEBKWZJZFAQXYSLUMNZBWTVDGCCDWIMTDFJAUQRCQNLRINVYIWVVYOJQGBCTZYYQRVVCUFANTNGCQTNVFWCWZLAQRCUIGBGBCIWAAVKLIQAOQXRMMUQNVRTXJQVRFNAPZWDAMCALGBFNARTDYUFVQWPOFFVQCRYLYPRAKNCTNGPGVMLPBCUOOZQGMVRCTTQRQRLNVIWKMCRIAVGBYSLRFRBCXAVWPGCAMDCKDCFAHZRBGXMSWTIMZBBWUSPMMPWPDGSCRLYOTJIYQVDJJAGZCXEJZUMTOFJPRIPYMGWNZFOPFVQTQNEJZFQTKLITBWMSLLNVBCXBYIHBCCYKQQLNOQQMCTKUCFAHXGBAFZTWJOBNLEQIRRFTBVICGIMBNLYFSAGMODMXBRUYOUFANTNXGLPGLTVGAMFMAGYXJLBJSQYQZMCMPTAFBJOQYWPSCNCFVQXTORYGAMCBRMMPWQUYSLVKQEJIPRITDFJIYBGBYYQBVKXFNAIWKMCFAUMUKGIVBBLSKYPRDGBWXIZMLSKFARDGBUFAFIACQNTIMTDFJLBKVYPXBBXROBTCGZKQFYIYBJYSLPUMFSBSWGAROYPIALKDUFAFWOOQJKBVFCZJNBZGRCXMRUGNYGTRBQWMAMBVYOJQERTNRCXIVLCDJFAGLWDWKQEAVKLIXYMCCSWMNNVOPBIELUKQDWHUKQFYPNDGCYNLLWWBQJTSAKVTJZYMVEQTDRZJKSQBUMUONFBVMPDQTNLWWBQFUBUGXRFNGMTGYWLFPGRYIMABGBCIBUMDVMHSUWWCCFVQEKDFTVROTSKSWQBQWCUZBKGOBJLJQVRFNAJWTUYRWAOVRCXQPSJOQJMZMFELIMEVQKNUZRPGXQNWABJYSLPUMOEQYPNDGULTEABJKRMQFTKPCFUBVIDFJARBTOYHPRZQEQIMZWPCBJXRVFOBTVNPCSPFVQPGBYYBYMFYLYWUQUZYYQRVVCYXQSPGGCWMCIASLLIAWTNGSIEGRBMKMFAKYLFTIQUSRNVNYWSCYMAONSQMNNUKVWMQFUCXLJZVAWZNTARZGKAYMQWPDFJURVHYPYPRGDOFFDRLVYFNUNAKPLTBUQPQFFLBKEEPWMQIUSDMMJMTOQYQYTURGUAQWEDMWIALVRCDAGQNVDFQGPHEJMIALULCKWEMVRCRIFBAYSWMQWKXEBMYTOIDWQRVFRCXIVLVYRMMSMNVMBEVBJDFJJNVFKEJLUMCNYSLVNGFCWIAGROPXWAPCNYHTBAGCFFDRQVGYXGBCAYSWPRIFWSXBOMCCFFZQIUSPTVJMNVEJWEOGRMBOBMUSRDWHZGKNWMGBAMMQWHZEOPYIVVNIUMGLWWBJNDRZOKLNAHXUSBJLBEPNGIGBCVKIJBUIVWCIQPQPOBNLUMVKIJBUIVWCIQPQPOKJVNGGKWJAVZJORTWXQVCSWMRVQEEMZRBWBLJLZWTQYSJRKCEQJGBCUOCXQAKGSYRUHBKXCJZFLQMRTZBZRBGXWALQMRTZNAKZPJNRZVYAFTYQVCYDAQWEDMWTVDGCCDQAPKCNQMNACXRJAGECIGRIXMKDYUWVVVYDMWAWWBLTBGWNYQJIZIPPMWSVVIQCTZTMIYBGTRA"
    cipher = "XSIHAGSRPQJRXAMNOZDHVMEQVYUIQZVZDKYRVIITAERELZRXWXNVDEWSYEXCAMXLPCNHHYPOTPTMLISSPNWWYASIHXVASIMETXLFKJRTRJCSHTAILZYNEVVCTRBTHLMDKMOHQWELVTMLIJWCONPHDEYDEILTWHAKIEYHPNDIRYIGTAITLGFAGHKTZDNZXLPLJUGHWLOZRVLMPJJFMLIXEDDLLIDAPNZXLPQOOMLIWMIETRHDSJFYJYWPXRRMRELZMHSRWMBHMSZPVOHXQSZVIOPJSCWJMXWTLGZTAIVPZZLEIVDWOOHHEREKENREMPZTHYROIMSMEROEGLMLEELVDUIIYHJNXMRDYXHAEWEIWUMERZROHXMVMIHULIHHMOSTASVIOOMLIYEOUKISQXCEWIIOACIVLALWGIDIXZFZDHRIFTJNMLIXSJREEROWZVXVCELDNZAEDRJWBREYYKRHEVDSHEVEPWMIGYSVELZIKTMDXJLLWSXIAOKXLPMMHHVWPWVNWWSXIAOKERZXCEKJPLWFOYAMYIWUMEXWIIGMLWZQZSXRWPGVMXFENOOOMLITVXRTDIOQDNWWEYHOHXALZPZOYXLPQOHBVXPIIIGRYXFZRMSSVLJRLIEYHNTTVXPHDNIYVDYDTMLIXSJNLLSYIXLXEVLFJVXXLPQVNWXLPCMOWIWHMATECEMVZALXXLODNZXLLXXONVWPACIVLXSIHABHQFWONXIHDLVVXXEVIIIYWLPAZRXXSCIVCALICSRNASQPXCERLEOKJNXEQTPZOKXAZACEGXLPCKALWIOSIEHJXSIIIZLXDLZPAIVOWPPHRXSIHOHVPLRYSTRHELZYVVMPHOOAMQESFNHAMQLZHTHWPIITAILFROAGHXSIHAGEWELZSMSVJKJELAEDWJCKEDPHRIMLJPEMTAEXSIXONPHDGVRVIWAIVKUYXLXGALXLPWVIWXLLXCEAEHTRYEXHWPIITAIYYLVPICQLMYEGAMELOHXLSFRYSNTSYLZRMVENOWUMMLLZZSXIRXSMEMLEYXCAMWETHCEYSVSYBOUEWVIMVBPPPTVSLIHXIPPHRLTWWLTGOXEMETRHELZRXVEYQPTXFISMIDAMQDYXHTLSFRYOYLIWPVSZSHQSMBBHWSSPLWIZPVWETXQJLZEEWWZXCEWVYYOZNLUYTVZSVYVDIYTAIWSIKHXVHLRYRHHIZRRAKHFFXNOHRXSIDRLOMYWOUKRIOGJLWJSCXCEKIGLQZAZEPWSKIGKENVJSLXLPQJOKEROXCEUPENOHAKIHLFWLXHATXCWAMXPJMOMLAPROPTWXHMOHMVETPDNZFVTHGETRHPQKTRWEOHGEMLIYXCEKIZPPGEKWVZHZCESWPXJGXXLPVAOKEKCIVTYIECAVSHRXSIHBNXXSITSMMPWJJLESAPHJVXVXSIHOHVXSSPGAIENLCAWLIMIZNTPSYIRONPHSEQEUIIYVDGAXKWEYTHLEGIOUKRIOLDSASVDINHXEHCMYIGKWWSRLRMRELDSYEWSMJNMLIJGVMXEXWENTNTSYXCEASYYHNTAIWPXCONKLVRJWGJSCXCEBVZLPJUKEROXCEBVFCIZDPIVPACIFTICMIGBRENPPSMIVLXOHXLILHJFTHIPTYIISVRSTAEEWHIXAEPMEYKOGXLPQJOKWSXINLBROTRBAPECLRYSHQIHMOHLXECXDNZLENOGELEROWOAKMRRITELKEKMIGWSAYXCEGEVCSRVTPPPCWEYSVPXCEFXLPGJMIERJLVDVSQPXJAAEPEQJRXWSMIMMXREDCJUFECRYZSLXLLRRHXRXSITSMEVEIYTAIQZWOOYXLPQRONPHMCIOFIEYWVDOERNIWUMXLCIZOYXLPQOHXFSWHZSMSVTXHARFIELZMHWXOVPNDIRCSYEYSVHEMDWSAYXCEZSCLPIOPMXZTZNXHMYXJAUVSLHNPTGITRRHBGLDXJOWXAZSATASWPKMETXWESIELWXTPGTHFIDIZNMLICIRHBGLHIMELIXMCXEKXETRAOKKSEXZ"
    # cipher = "ahylygcdsoegqbzyafjlpmgrhwtlagndnbzqchfgatvqzojbohvpuclqasuwkpvdxzvwkhyljyclgsrqwhkdyyvuwbuwdokljqcxzsjxjrvuohrqzwejpstkjwhxagkkwhtdjpvxosuwkqfplffpegvvaqluehpkkkvyaflvebxwdcjhpstkjwhxagzqpvvuaoczkfcgiopyeccdpskkazrzkfkkaielrsivehpvnichooegehddupvxjskkeqroqbuhngfpaqzuyidvpoefagvyabgukpzqctfussrnjsjvagddufvvqzkljgvyafvsabropwvvqdkrwbuljqcxzwejalgxhgzrjqzyezwljsjdjradezklisfxndfoeqpljsvfowjwdokbkidxohihodvfphyhlfzywqpdjrgukdvupmilcvkvktfwdsivwhrohhzpagfuazjhuclzezciwwcwdstrqfjhwqkljucdstlohmrqzskkeqrohmzvuclunsjskbjlxwclpmtdnswxhzpuaouwdstridlwafwuwiudjrreqgvdyhtiworiarvuwzjwwhlwahydppirwrcbyfzpebroenvvycdsqhvuebkuqgzrjhylowjrjsfiosmhnocowkjwdokjkjvujvrfgwejqbuhngkdjrnkwhkkazrzlffkepzwowwljrfxxhnhyoeuatvuuclwkoedphfujspshsrvafvyesnlpgjskzzfesjrjfvvlcevepchqgvrbhvfdbfokupuagfxnqvvwbufwsevlcclymuryidhjhjikfxxervoebvvycefafeljugukdvu".upper()
    #################################################################
    # Your code to determine the key and decrypt the ciphertext here
    
    # print(pop_var(alphabet))
    # alphabetFreq = np.array(list(letter_freqs.values()))
    # print(bestShift(np.roll(alphabetFreq,20)))
    # print(letterFreq(alphabet))
    
    slicedCipher = [None] * 12
    cipherWords = [None] * 12
    for i in range(2,14):
        slicedCipher[i-2] = [""] * (i)
        cipherWords[i-2] = [0] * (i)
    words = [None] * 12
    for i in range(len(cipher)):
        for keyLength in range(2,14):
            slicedCipher[keyLength-2][i%(keyLength)] = slicedCipher[keyLength-2][i%(keyLength)] + cipher[i]
    
    for i in range(12):
        word = ""
        for j in range(len(slicedCipher[i])):
            word = word + (value2Letter(bestShiftTest(letterFreq(slicedCipher[i][j]))))
        words[i] = word 
    
    
    
    
    
    
    freq = [0]*12
    for i in range(12):
        for j in range(len(slicedCipher[i])):
            freq[i] += pop_var(slicedCipher[i][j])

    for i in range(12):
        freq[i] = freq[i]/(len(slicedCipher[i]))

    freqVarCipher = pop_var(cipher)
    

    index = freq.index(max(freq))
    key = words[index]
    print(key)


