
<script setup lang="ts">
    import 'bootstrap/dist/css/bootstrap.min.css';
    import $ from 'jquery';

    
    import { ref } from "vue";
    import type {Ref} from "vue";
    
 
    

    let show_picture:Ref<boolean> = ref(true) //default value


    let change_show = (value:string,event:any) => {


        //change click event text decoration
        $(".Select_menu_type_selection span").css("border-bottom","none")
        $(event.target).css("border-bottom","solid")


        if (value == "picture"){
            show_picture.value = true
        }else{
            show_picture.value = false
        }
        
    }


    

    $(document).ready(function () {
        Get_menu_data();
        get_food_types();
    })

    let food_type_datas:any = ref([]);
    let get_food_types = async () => {
        let api_headers = {

            method: 'GET',
            headers: {
                'Content-Type': 'application/json'
            }
        }
        try {
                // data = await fetch('https://xiao-suan-tao-backend-cc9d64416e53.herokuapp.com/api/FoodType/', api_headers)
                let data = await fetch('http://127.0.0.1:8000/api/FoodType/',api_headers)
                .then((res) => {



                    return res.json()
                })



            

            for (let index = 0; index < data.length; index++) {
                food_type_datas.value.push(data[index]['type_name']);
                
            }

            console.log(food_type_datas.value)
            




        } catch (error) {

            console.log(error)
        }
    }

    
    
    let menu_data = ref();
    let Get_menu_data = async() =>{

        let api_headers = {
    
            method: 'GET',
            headers: {
            'Content-Type': 'application/json'
            }
        }
        try {
            let data = await fetch('https://xiao-suan-tao-backend-cc9d64416e53.herokuapp.com/api/Menu/',api_headers)
            //let data = await fetch('http://127.0.0.1:8000/api/Menu/',api_headers)
            .then((res)=>{

                
                
                return res.json()
            })
            
            

            console.log(data)
            menu_data.value = await data;
          



        } catch (error) {

            console.log(error)
        }

    }


    

    let Langauge_CH:Ref<boolean> = ref(true)
    let Langauge_EN:Ref<boolean> = ref(false)
    let Langauge_IN:Ref<boolean> = ref(false)

    let change_lang = () =>{

        
        //change click event text decoration
        let type = $('.form-select').find(":selected").val();
        

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

        console.log(Langauge_CH.value,Langauge_EN.value,Langauge_IN.value)
    }

    


    let food_type = ref("全部")
    let fileter_food_types = (type:string) =>{
        food_type.value = type
        
    }

    
</script>
<style lang="scss">
    @import "@/assets/css/menu.scss";
</style>

<template>
    <div id="menu_background">






        <div class="Select_menu_type">

            <div class="Select_menu_type_selection">

                <span @click="change_show('picture',$event)" style="border-bottom: solid;">圖片菜單</span>
                <span>｜</span>
                <span @click="change_show('list',$event)">紙本菜單</span>
            </div>

           

        </div>

        
        
        
        <div v-show="show_picture" class="menu_foods_grounp"><!-- display menu-->
            <p class="Our_menu"> Our Menu </p>

            <span class="Languge_title">Languge: </span>
            <select class="form-select" aria-label="Default select example" @change="change_lang()">
                <option value="CH" selected>繁體中文</option>
                <option value="EN">English</option>
                <option value="IN">Indonesian</option>
                </select>
            
            
            
            <div class="food_type">
                <span @click="fileter_food_types('全部')">全部</span>
                <span  v-for="item in food_type_datas" :key="item" @click="fileter_food_types(item)">{{item}}</span>
                

            </div>

            <div v-for="item in menu_data" :key="item" class="menu_food">

                <div  v-if="food_type == item.food_types || food_type == '全部'" class="food_type_group">

                    <img :src="item.menu_picture" alt="" ><!--food pictures-->
                    


                    
                    <div class="menu_naming"> <!-- lang type-->
                        <div v-show="Langauge_CH">
                        {{ item.name_ch }}
                        <p>{{ item.Custom_unit }}</p>
                        <p>{{ item.Custom_price }}</p>
                        </div>

                        <div v-show="Langauge_EN">

                            {{ item.name_EN }}
                            <p>{{ item.Custom_price }}</p>
                        </div>
                        
                        <div v-show="Langauge_IN">

                            {{ item.name_Indonesian }}
                            <p>{{ item.Custom_price }}</p>
                        </div>

                    </div>


                    

                    
                    
                    
                
                </div>

                
            </div>
            
        </div>


        <div  v-show="!show_picture" class="list_menu_display"><!-- display list-->

            <img src="@/assets/img/2024-05-13_menu_list.png" alt="" >

        </div>


        
    </div>
</template>