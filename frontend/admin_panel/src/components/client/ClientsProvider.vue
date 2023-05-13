<template>
    <v-container>
        <div class="text-h3 py-6 mx-10 text-left"> Поставщик: {{ name_p }} </div>
        <v-btn  variant="outlined" class="mx-10" :to="{name: 'ClientProviders'}">
            <v-icon icon="mdi-arrow-collapse-left" color="deep-orange" class="mr-2"></v-icon>назад
        </v-btn>
        <v-container>
            <v-col>
                <div class="text-h5 py-6 mx-10 text-left">Адрес:</div>
                <v-card class="my-2 pa-6 mx-14 d-flex flex-row" variant="outlined">
                    <b class="pr-2">Город:</b> {{ this.town }}
                    <v-spacer></v-spacer>
                    <b class="pr-2">Улица:</b> {{ this.street_adr }}
                    <v-spacer></v-spacer>
                    <b class="pr-2">Дом:</b> {{ this.house_adr }}
                    <v-spacer></v-spacer>
                    <b class="pr-2">Корпус:</b> {{ this.frame_adr }}
                    <v-spacer></v-spacer>
                    <b class="pr-2">Индекс:</b> {{ this.index_addr }}
                </v-card>
                <div class="text-h5 py-6 mx-10 text-left">Расположение на карте:</div>

                <div class="map ml-15">
                    <yandex-map
                        :coords="[this.latitude_adr, this.longitude_adr]"
                        :zoom="16"
                    >
                        <ymap-marker 
                            :coords="[this.latitude_adr, this.longitude_adr]" 
                            marker-id="1" 
                            :icon="{ color: 'red' }"
                        />
                    </yandex-map>
                </div>

                <div class="text-h5 py-6 mx-10 text-left">Категории:</div>
                <v-row>
                    <v-col
                                v-for="cat in categories"
                                :key="cat.id_cat"
                                cols="12"
                                md="3"
                                v-bind="props_hover"
                    >    
                        <v-hover v-slot="{ isHovering, props }" >
                            <v-card 
                                v-bind="props"
                                class="my-3 pa-6 mx-14 d-flex flex-row justify-center"
                                :color="isHovering ? 'deep-orange': undefined"
                                variant="outlined"
                                :to="{ name: 'ProviderCategory', params: {id_p: this.$route.params.id_p, cat_id: cat.id_cat}}"
                                
                            >
                                <v-card-title>
                                    {{ cat.name_cat }}
                                </v-card-title>
                            </v-card>
                        </v-hover>
                    </v-col>
                </v-row>
            </v-col>
        </v-container>
    </v-container>
</template>

<script>
import axios from 'axios';

export default{
    data(){
        return{
            name_p: "",
            town: "",
            street_adr: "",
            house_adr: "",
            frame_adr: "",
            longitude_adr: "",
            latitude_adr: "",
            index_addr: "",
            categories: []
        }

    },

    methods: {
        get_data_about_provide(){
            axios.get(`http://127.0.0.1:5000/admin_panel/api/v1.0/suppliers/${this.$route.params.id_p}`)
            .then( response => (
                this.name_p = response.data.name_p,
                this.town = response.data.town,
                this.street_adr = response.data.street_adr,
                this.house_adr = response.data.house_adr,
                this.frame_adr = response.data.frame_adr,
                this.longitude_adr = response.data.longitude_adr,
                this.latitude_adr = response.data.latitude_adr,
                this.index_addr = response.data.index_addr,
                this.categories = response.data.categories
            ))
        }
    },

    mounted(){
        this.get_data_about_provide()
    },

    updated(){
        this.get_data_about_provide()
    }
}
</script>

<style scoped>
.ymap-container {
    width: 1600px;
    height: 500px;
}

</style>