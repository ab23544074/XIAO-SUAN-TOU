
<script setup lang="ts">
    import "@/assets/js/menu.ts";
    
    import $ from 'jquery';
    

    
    import { ref } from "vue";
    import type {Ref} from "vue";
    
    

    let show_picture:Ref<boolean> = ref(true) //default value


    let change_show = (value:string) => {
        if (value == "picture"){
            show_picture.value = true
        }else{
            show_picture.value = false
        }
        
    }


    

    $(document).ready(function () {
        Get_menu_data()
    })



    

    let menu_data = ref();
    let Get_menu_data = async() =>{

        let api_headers = {
    
            method: 'GET',
            headers: {
            'Content-Type': 'application/json'
            }
        }
        try {
            let data = await fetch('http://localhost:8000/api/Menu/',api_headers)
            .then((res)=>{

                
            
                return res.json()
            })
            
            

            
            menu_data.value = await data;




        } catch (error) {

            console.log(error)
        }

    }


    

    let Langauge_CH:Ref<boolean> = ref(true)
    let Langauge_EN:Ref<boolean> = ref(false)
    let Langauge_IN:Ref<boolean> = ref(false)

    let change_lang = (type:string) =>{


        if (type == "CH"){

            // change menu display langauge
            Langauge_CH.value = true
            Langauge_EN.value = false
            Langauge_IN.value = false


            

            
        }else if(type == "EN"){
            Langauge_CH.value = false
            Langauge_EN.value = true
            Langauge_IN.value = false
        }else{
            Langauge_CH.value = false
            Langauge_EN.value = false
            Langauge_IN.value = true
        }
    }

    let Selected_food_data = [{
            food_title:"酥炸魷魚絲",
            description:"酥脆香甜、口感Q彈<br>\
                            搭配小蒜頭特製胡椒<br>\
                            是許顧客必買的項目<br>",
            picture:"src/assets/img/魷魚絲.png"
        },
        {
            food_title:"酥炸鹹酥雞",
            description:"傳統醃漬手法 <br>\
                        加上代骨雞肉<br>\
                        一口吃下滿滿的醬香和肉香<br>\
                        是許顧客必買商品<br>",
            picture:"src/assets/img/鹹酥雞.png"

        },
        {
            food_title:"七里香、雞胗、雞心",
            description:"特殊醃料配上酥脆油炸手法<br>\
                    去除腥味的同時<br>\
                    保留肉味的香氣<br>\
                    許多害怕內臟類的顧客也敢嘗試<br>",
            picture:"src/assets/img/串串.png"
        }

    ]

    

     
</script>
<style lang="scss">
    @import "../assets/css/menu.scss";
</style>

<template>
    <div id="menu_background">

        <div class="choose_lang row">
            <div class="col-lg-12"> Menu  Langauge </div>
            
            <div class="lang_selection col-lg-12">
                <span @click="change_lang('CH')" :class="{display_underline:Langauge_CH}"> 繁體中文 </span>
                <span @click="change_lang('EN')" :class="{display_underline:Langauge_EN}"> English </span>
                <span @click="change_lang('IN')" :class="{display_underline:Langauge_IN}"> Indonesian </span>

            </div>
            
        </div>
        
        
        <div class="Selected-food row" >
            <h2> 精選美食</h2>
            
            
            
            <div class="Selected-food-gorup" v-for="item in Selected_food_data">

                <div class="Selected_food_title">

                    {{item.food_title}}
                

                </div>

                
                
                <div class="Selected_food_description" v-html="item.description">
                    

                </div>


                <div class="Selected_food_picture"> 
                    <img :src=item.picture alt="">

                </div>
                

                

            </div>

            

        </div><!--Selected-food-->



        <div class="Select_menu_type">

            <div class="Select_menu_type_selection">

                <span @click="change_show('picture')" :class="{display_underline:show_picture}">圖片菜單</span>
                <span>｜</span>
                <span @click="change_show('list')" :class="{display_underline:!show_picture}">紙本菜單</span>
            </div>

           

        </div>
        
        
        <div v-show="show_picture" class="menu_foods_grounp"><!-- display menu-->

            <div v-for="item in menu_data" class="menu_food">

                <img :src="item.menu_picture" alt="" ><!--food pictures-->

                <div class="menu_naming"> <!-- lang type-->
                    <div v-show="Langauge_CH">
                    {{ item.name_ch }}
                    </div>

                    <div v-show="Langauge_EN">

                        {{ item.name_EN }}
                    </div>
                    
                    <div v-show="Langauge_IN">

                        {{ item.name_Indonesian }}
                    </div>

                </div>
                
                
                
                
                
                
                {{ item.Custom_unit }}
                {{ item.Custom_price }}
                

            </div>
            
        </div>


        <div  v-show="!show_picture" class="list_menu_display"><!-- display list-->

            <img src="@/assets/img/2024-05-13_menu_list.png" alt=""></img>

        </div>


        
    </div>
</template>