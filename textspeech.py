from gtts import gTTS
import os
import time
txt="Welcome to the Story Time. DRAMA ARTIST AND HIS DIAMOND. Once upon a time one Drama Artist from India went to London to show his talent. He showed his talent to the people, All the people were mesmerized because he changed his make up every time. Suddenly he disguised as a girl,suddenly he disguised as a boy, and suddenly he disguised as an old man. So people were mesmerized and they gave him a lot of money. He earned more money in London,nearly one crore.He thought how to take this much of money to India. He decided to buy a Diamond with a value of one crore. So he bought a most beautiful Diamond with his money. He returned back to India.There was no flight in those days because Aeroplane was not found yet. So he decided to go by the ship for sea travel.Travelling in ship took more than a week. He thought,to show his talent in the ship.So he can also earn more money.He started to show his talent in the ship also. All people in the ship also saw his talent and they were amazed. At that time He thought to show his talent with his Diamond. So He took out his Diamond and showed that beautifullness. All the peoples saw with mouth opened. Then He threw it up to the sky and catched it. It was very beautiful because rainbow colors came out from inside the Diamond. People were mesmerized and amazed. So he tryed to throw the Diamond more higher to the sky. But Suddenly the ship shook and the Diamond fell down into the deep sea. No one could take it because it was very deep like two mountains deep. So Drama Artist fedup and went to his bed with a sad face.The Moral.From this story what we learn is ,Drama Artist lose his valuable Diamond into the deep sea,like him  we should not lose our soul. Because our soul is very important for everybody. If we do the sin and lose our soul into satan, Our life is waste. we have to keep the soul with out sin. Unfortunately or unkownly if we do the sin,the only way is Lord jesus. He is the one and only God, he who victory the satan. For the wages of sin is death; but the gift of God is eternal life through Jesus Christ our Lord. Romans 6:23" 
lang="en"
x=gTTS(text=txt,lang=lang,slow=False)
x.save("welcome.mp3")
os.system("start welcome.mp3")







