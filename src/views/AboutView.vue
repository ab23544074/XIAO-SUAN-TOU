<script setup lang="ts">
import "@/assets/css/about.scss";
import "@/assets/js/about"

import 'bootstrap/dist/css/bootstrap.min.css';
import {onMounted, ref} from 'vue';
import 'animate.css';
import $ from 'jquery';








let story:any = [{
    
    "description":"學生時代到處打工，沖床、台灣涼椅、餐廳外場內場、組Band、駐唱、那卡西，\
                    ---好像很多，但無一專精！後來記得母親時常跟我講的話（一支草一點露、人無艱苦過，難得世間才），覺得我不僅是如此，\
                    我如果繼續這樣，會對不起自己（雖然目前比上不足，比下有餘）。年輕的衝勁隨著年齡的增長而慢慢地淡化！\
                    最後我選擇了自行創業（腦海浮現：我不能输人家）。",
    
    "picture": new URL("@/assets/img/about_story1.jpg", import.meta.url).href,



    },

    {
    
    "description":"開店的第一家店址在東安戲院旁，跟自助餐的老闆分租，做了2個月，房東說騎樓不給擺攤（因為他旁邊還有兩格沒租出去），後來就搬到歸仁的現址（我二哥幫我找的）。\
                剛開始賣的第一天營收2400，高興死了，比東安戲院旁好很多（除了中秋節當天），後來業績一個月比一個月好。\
                但到冬天寒流來時都沒人光顧。有一次深刻的體驗：我騎著摩托車（武車）載著一車的貨去出攤，那天寒流來襲又下雨，只賣了2百多塊，收攤之後又載一車的貨回去，天空又下著雨，又冷又濕，不自覺落下眼淚（不知道是雨水還是淚水），自今我還依稀記得那時的心情-------好像淚又來了！\
                    最後我選擇了自行創業（腦海浮現：我不能输人家）。",
    
    "picture": new URL("@/assets/img/about_story2.jpg", import.meta.url).href ,



    },



    {
    
    "description":" 後來業績蒸蒸日上，結婚之後有個賢內助幫我打理很多事，才能夠維持到現在。當然一雙兒女從國小之後有空就來幫忙，分擔我們小蒜頭的事務也給他（她）們按個讚！",
    
    "picture": new URL("@/assets/img/about_story3.png", import.meta.url).href,



    },


    {
    
    "description":" 目前兒子承接小蒜頭的工作，女兒也有自己的一片天，我夫妻倆就在不久的將來準備退休好好過老年生活。\
                    感謝各位捧場的客人，不吝指教的客人；還有親朋好友，我們可愛的歷年員工，有你（妳）們真好！\
                    謝謝您！！！",
    
    "picture": new URL("@/assets/img/about_story4.png", import.meta.url).href ,



    },



]


let histroy:any = [{
            "TIME": "民國82年/8月",
            "DESCRIPTION": "成立於台南市長榮路一段（新崇安戲院旁）",
            "PICTURE": new URL("@/assets/img/東安戲院.jpg", import.meta.url).href 
        },
        {
            "TIME": "民國82年/10月",
            "DESCRIPTION": "搬遷至台南縣歸仁（中正路與復興路口）",
            "PICTURE": new URL("@/assets/img/歸仁店.svg", import.meta.url).href 
        },
        {
            "TIME": "民國85年",
            "DESCRIPTION": "台南關廟第一家分店成立（民國111年閉幕)",
            "PICTURE": ""
        },
        {
            "TIME": "民國92年",
            "DESCRIPTION": "台南新化店分店成立",
            "PICTURE": new URL("@/assets/img/新化分店.svg", import.meta.url).href 
        },
        {
            "TIME": "民國113年",
            "DESCRIPTION": "台南新關廟店成立",
            "PICTURE": new URL("@/assets/img/關廟新店.jpg", import.meta.url).href  
        },

        ]




   
    
        
   
</script>

<style scoped>
    
</style>
<template>


    <h1 class="wow animate__animated animate__fadeIn story_title" >老闆的故事</h1>
 
    
    <div class="first container-fluid row " v-for="item in story" :key="item">

       


        <div class="col-lg-3 first_picture">

        
            <img :src="item.picture" alt="" class="about_1">

        </div>

        <div  class="col-lg-9">

            


            <div class="about_description wow animate__animated animate__zoomIn">
                {{ item.description }}

                

            </div>
        </div>
    </div>




    

    <div class="second container-fluid row m-0 p-0">



        <div  class="col-lg-12 history">

            <h1  class="wow animate__animated animate__fadeIn">我們的朋友</h1>

            
            <div class="arrow"></div>

                
            <div class="history_text" >

                <!--1-->

                <div v-for="item in histroy" :key="item" class="history_group">

                    
                    <p class="history_time wow animate__animated animate__fadeIn animate__slower">{{item.TIME}}</p>
                    <p class="history_time wow animate__animated animate__fadeIn animate__slower">{{item.DESCRIPTION}}</p>
                    
                    
                    <div class="history_pic wow animate__animated animate__fadeIn animate__slower" v-if="item.PICTURE">
                        <img :src="item.PICTURE" alt="" class=" ">
                    </div>

                </div>


            </div>
            
            
           <!-- <img src="@/assets/img/about_history.svg" alt="">-->

            
        </div>


       

    </div>
</template>