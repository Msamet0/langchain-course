from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_ollama import ChatOllama

load_dotenv()

def main():
    print("Hello from langchain-course!")
    information = """
    Elon Reeve Musk (/ˈiːlɒn/ EE-lon; 28 Haziran 1971 doğumlu), Tesla, SpaceX, X ve xAI şirketlerinde liderliğiyle tanınan bir iş insanı ve girişimcidir. Musk, 2021'den beri dünyanın en zengin kişisi oldu; Aralık 2025 itibarıyla, Forbes, net servetinin yaklaşık 754 milyar ABD doları olduğunu tahmin ediyor.

Pretoria, Güney Afrika'da zengin bir ailede doğan Musk, 1989'da Kanada'ya göç etti; annesi orada doğduğundan beri Kanada vatandaşlığına sahiptir. 1997 yılında Amerika Birleşik Devletleri'nin Philadelphia kentindeki Pennsylvania Üniversitesi'nden lisans derecesi aldı, ardından iş girişimlerine başlamak için Kaliforniya'ya taşındı. 1995 yılında Musk, yazılım şirketi Zip2'yi kurdu. 1999'daki satışının ardından, daha sonra birleşerek PayPal'ı oluşturan ve 2002'de eBay tarafından satın alınan X.com adlı çevrimiçi ödeme şirketini kurdu. Musk ayrıca 2002 yılında Amerikan vatandaşı oldu.

2002 yılında Musk, uzay teknolojisi şirketi SpaceX'i kurdu ve CEO'su ile baş mühendis oldu; Şirket, o zamandan beri yeniden kullanılabilir roketler ve ticari uzay uçuşlarında yeniliklere öncülük etti. Musk, 2004 yılında otomobil üreticisi Tesla'ya erken yatırımcı olarak katıldı ve 2008'de CEO'su ve ürün mimarı oldu; O zamandan beri elektrikli araçlarda lider haline geldi. 2015 yılında yapay zeka (YD) araştırmalarını ilerletmek için OpenAI'yi kurdu, ancak daha sonra ayrıldı; 2020'lerde örgütün yönüne ve liderliğine artan memnuniyetsizlik, onu xAI'yi kurmaya yönlendirdi. 2022'de Twitter'ı satın aldı, önemli değişiklikler yaptı ve 2023'te X olarak yeniden markalaştı. Diğer iş yerleri arasında 2016'da kurduğu nöroteknoloji şirketi Neuralink ve 2017'de kurduğu tünel şirketi Boring Company bulunmaktadır. Kasım 2025'te, Musk için 1 trilyon dolarlık bir Tesla ödeme paketi onaylandı; belirli hedeflere ulaşırsa bu paketi 10 yıl boyunca alacak.

Musk, 2024 ABD başkanlık seçimlerinde Donald Trump'ı desteklediği en büyük bağışçıydı. Trump 2025 başlarında başkan olarak göreve başladıktan sonra, Musk Başkan'ın Kıdemli Danışmanı ve Hükümet Verimliliği Departmanı'nın (DOGE) fiili başkanı olarak görev yaptı. Trump ile yaşanan kamu anlaşmazlığının ardından Musk, Trump yönetiminden ayrıldı ve şirketlerini yönetmeye geri döndü.

Musk, küresel aşırı sağ figürlerin, davaların ve siyasi partilerin destekçisidir. Siyasi faaliyetleri, görüşleri ve açıklamaları onu kutuplaştırıcı bir figür haline getirdi. Musk, COVID-19 ile ilgili yanlış bilgiler, komplo teorilerini yaymak ve antisemitik, ırkçı ve transfobik yorumları doğrulamakla eleştirildi. Twitter'ı satın alması, sansürü azaltma taahhüdü sonrası nefret söyleminin artması ve hizmette yanlış bilginin yayılması nedeniyle tartışmalı oldu. İkinci Trump yönetimindeki rolü, özellikle DOGE'ye karşı kamuoyunun tepkisine yol açtı.
    """
    summary_template = """
    given the informaion {information} about a person I want you create:
    1.A short summary 
    2. two intersting facts about them
    3. answer only in turkish
    """
    summary_prompt_template = PromptTemplate(
        input_variables=["information"],template=summary_template
    )

    llm = ChatGoogleGenerativeAI(temperature=0,  model="gemini-2.5-flash-lite",)
    #llm = ChatOllama(temperature=0, model="gemma3:270m")

    chain = summary_prompt_template | llm

    response = chain.invoke(input={"information": information})
    print(response.content)

if __name__ == "__main__":
    main()
