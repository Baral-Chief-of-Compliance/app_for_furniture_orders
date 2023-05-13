<template>
    <v-container>
            <div class="text-h3 py-6 mx-10 text-left">Поставщики</div>

            <v-container class="d-flex justify-center">
                    <v-row class="mx-10">
                        <v-col
                            v-for="el in providers"
                            :key="el.id_p"
                            cols="12"
                            md="3"
                            v-bind="props_hover"
                        >    
                            <v-hover v-slot="{ isHovering, props }">
                                <v-card v-bind="props" height="200" width="300" 
                                    class="mx-auto mb-10 d-flex justify-center" 
                                    :color="isHovering ? 'deep-orange' : undefined"
                                    :to="{ name: 'ClientProvider', params: {id_p: el.id_p}}"
                                    variant="outlined"
                                >
                                <v-card-item class="text-h6">
                                    {{ el.name_p }}
                                </v-card-item>
                
                                </v-card>

                            </v-hover>
                        </v-col>
                    </v-row>
            </v-container>
    
    </v-container>
</template>

<script>
import axios from 'axios';


export default{
    data(){
        return{
            providers: []
        }
    },

    methods: {
        get_all_providers(){
            axios.get("http://127.0.0.1:5000/admin_panel/api/v1.0/suppliers")
            .then(response => (this.providers = response.data))
        }
    },

    mounted(){
        this.get_all_providers()
    },

    updated(){
        this.get_all_providers()
    }
}
</script>