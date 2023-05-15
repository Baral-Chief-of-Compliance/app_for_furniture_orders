<template>
    <v-container>
        <div class="text-h3 py-6 mx-10 text-left"> Поставщик: {{ this.name_p }} </div>
        <div class="text-h4 py-6 mx-10 text-left"> Категория: {{ this.name_cat }} </div>
        <div class="text-h5 py-6 mx-10 text-left"> Товар: {{ this.name_product }} </div>
        <v-btn  variant="outlined" class="mx-10" :to="{name: 'ProviderCategory', params: {id_p: this.$route.params.id_p, cat_id: this.$route.params.cat_id}}">
            <v-icon icon="mdi-arrow-collapse-left" color="deep-orange" class="mr-2"></v-icon>назад
        </v-btn>
        <v-col>
            <v-card
                class="my-2 pa-6 mx-14 d-flex flex-row" 
                variant="outlined" 
            >
                    <b class="pr-2">Цена:</b> {{ this.price_product }} <b class="pl-2">руб.</b>
                    <v-spacer></v-spacer>
                    <b class="pr-2">Осталось:</b> {{ this.quantity_product }} <b class="pl-2">штук</b>
                    <v-spacer></v-spacer>
                    <b class="pr-2">Рейтинг:</b> 
                        <v-icon color="yellow" icon="mdi-star"/> 
                        <v-icon color="yellow" icon="mdi-star"/>
                        <v-icon color="yellow" icon="mdi-star"/>
                        <v-icon color="yellow" icon="mdi-star"/>
                        <v-icon color="yellow" icon="mdi-star"/>
                    <b class="pl-2">баллов</b>
            </v-card>
            <div class="text-h5 py-6 mx-10 text-left">Описание:</div>
            <v-card
                class="my-2 pa-6 mx-14 d-flex flex-row" 
                variant="outlined" 
            >
                {{ this.description_product }}
            </v-card>

            <div class="text-h5 py-6 mx-10 text-left">Параметры:</div>
            <v-card
                class="my-2 pa-6 mx-14 d-flex flex-row" 
                variant="outlined" 
            >
                    <b class="pr-2">Цвет:</b> {{ this.color_product }}
                    <v-spacer></v-spacer>
                    <b class="pr-2">Высота:</b> {{ this.height_product }} <b class="pl-2">см.</b>
                    <v-spacer></v-spacer>
                    <b class="pr-2">Ширина:</b> {{ this.width_product }} <b class="pl-2">см.</b>
                    <v-spacer></v-spacer>
                    <b class="pr-2">Длинна:</b> {{ this.long_product }} <b class="pl-2">см.</b>
            </v-card>

            <v-row class="mx-14 mt-15">
                <v-dialog
                    v-model="dialog"
                    width="auto"
                >
                    <template v-slot:activator="{ props }">
                        <v-btn  block
                            color="green-accent-4"
                            v-bind="props"
                        >
                            Добавить в корзину
                        </v-btn>
                    </template>    
                    
                    <v-card>
                        <v-card-title>
                            Введите количество товара
                        </v-card-title>
                        <v-card-text>
                            <v-text-field type="number" label="количество товара" variant="underlined"></v-text-field>
                        </v-card-text>
                        <v-card-actions>
                            <v-btn color="red" @click="dialog = false">Закрыть</v-btn>
                            <v-spacer></v-spacer>
                            <v-btn color="green" @click="dialog = false">Добавить в корзину</v-btn>
                        </v-card-actions>
                    </v-card>
                </v-dialog>
            </v-row>
        </v-col>
    </v-container>
</template>


<script>
import axios from 'axios'


export default{
    data(){
        return{
            name_p: "",
            name_cat: "",

            id_product: "",
            name_product: "",
            quantity_product: "",
            price_product: "",
            raiting_product: "",
            description_product: "",
            color_product: "",
            height_product: "",
            width_product: "",
            long_product: "",

            dialog: false
        }
    },

    mounted(){
        this.get_data_about_provide(),
        this.get_cat_name(),
        this.get_data_about_product()
    },

    update(){
        this.get_data_about_provide(),
        this.get_cat_name(),
        this.get_data_about_product()
    },

    methods: {
        get_data_about_provide(){
            axios.get(`http://127.0.0.1:5000/admin_panel/api/v1.0/suppliers/${this.$route.params.id_p}`)
            .then( response => (
                this.name_p = response.data.name_p
            ))
        },

        get_cat_name(){
            axios.get(`http://127.0.0.1:5000/admin_panel/api/v1.0/categories/${this.$route.params.cat_id}`)
            .then( response => (
                this.name_cat = response.data.name
            ))
        },

        get_data_about_product(){
            axios.get(`http://127.0.0.1:5000/admin_panel/api/v1.0/products/${this.$route.params.id_product}`)
            .then( response => (
                this.id_product = response.data.id_product,
                this.name_product = response.data.name_product,
                this.quantity_product = response.data.quantity_product,
                this.price_product = response.data.price_product,
                this.raiting_product = response.data.raiting_product,
                this.description_product = response.data.description_product,
                this.color_product = response.data.color_product,
                this.height_product = response.data.height_product,
                this.width_product = response.data.width_product,
                this.long_product = response.data.long_product
            )) 
        }
    }
}
</script>