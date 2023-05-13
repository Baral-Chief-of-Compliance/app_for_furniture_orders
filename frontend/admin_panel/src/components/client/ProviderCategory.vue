<template>
    <v-container>
        <div class="text-h3 py-6 mx-10 text-left"> Поставщик: {{ name_p }} </div>
        <div class="text-h4 py-6 mx-10 text-left"> Категория: {{ name_cat }} </div>
        <v-btn  variant="outlined" class="mx-10" :to="{name: 'ClientProvider', params: {id_p: this.$route.params.id_p}}">
            <v-icon icon="mdi-arrow-collapse-left" color="deep-orange" class="mr-2"></v-icon>назад
        </v-btn>

        <v-col>
            <div class="text-h5 py-6 mx-10 text-left">Товары:</div>
            <dvi v-for="pr in products" :key="pr.id_product">
                <v-hover v-slot="{ isHovering, props }" >
                <v-card 
                    class="my-2 pa-6 mx-14 d-flex flex-row" 
                    variant="outlined" 
                    v-bind="props"
                    :color="isHovering ? 'deep-orange': undefined"
                    :to="{name: 'ProviderProduct', params: {id_p: this.$route.params.id_p, cat_id: this.$route.params.cat_id, id_product:  pr.id_product}}"
                >
                    <b class="pr-2">Название:</b> {{ pr.name_product }}
                    <v-spacer></v-spacer>
                    <b class="pr-2">Количество:</b> {{ pr.quantity_product }}
                    <v-spacer></v-spacer>
                    <b class="pr-2">Цена:</b> {{ pr.price_product }} <b class="pl-2">руб</b>
                </v-card>
                </v-hover>
            </dvi>
        </v-col>
    </v-container>
</template>

<script>
import axios from 'axios';


export default{
    data(){
        return{
            name_p: "",
            name_cat: "",
            products: [] 
        }
    },

    methods: {
        get_data_about_provide(){
            axios.get(`http://127.0.0.1:5000/admin_panel/api/v1.0/suppliers/${this.$route.params.id_p}`)
            .then( response => (
                this.name_p = response.data.name_p
            ))
        },

        get_products(){
            axios.get(`http://127.0.0.1:5000/admin_panel/api/v1.0/categories/${this.$route.params.cat_id}`)
            .then( response => (
                this.name_cat = response.data.name,
                this.products = response.data.products
            ))
        }
    },

    mounted(){
        this.get_data_about_provide(),
        this.get_products()
    }
}
</script>