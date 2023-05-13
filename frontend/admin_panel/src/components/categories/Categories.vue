<template>
    <div class="text-center">
        <v-dialog
            v-model="dialog"
            width="auto"
        >
            <template v-slot:activator="{ props }">
                <div class="text-h3 py-6 mx-10 text-left">Категории товаров</div>

               
                <v-container class="d-flex justify-center">
                    <v-col>
                        <v-row class="mx-10">
                            <v-col  v-for="c in categories" cols="12" md="3"  v-bind="props_hover">
                                <v-hover v-slot="{ isHovering, props }" >
                                    <v-card  class="mx-auto" height="200" width="300" 
                                        v-bind="props"
                                        :color="isHovering ? 'amber': undefined"
                                        :to="{ name: 'category', params: {id: c.id_cat}}"
                                    >
                                        <v-card-item class="text-h6">
                                            {{ c.name_cat }}
                                        </v-card-item>
                                    </v-card>

                                    <v-card-actions class="mt-3">
                                        <v-spacer></v-spacer>
                                        <v-btn @click="delete_category(c.id_cat)" variant="outlined" color="red"
                                        >Удалить</v-btn>
                                    </v-card-actions>
                                </v-hover>
                            </v-col>
                        </v-row>    
                        <v-row class="mx-14 mt-15">
                            <v-btn  block
                                color="green-accent-4"
                                v-bind="props"
                            >
                                Добавить категорию товара
                                </v-btn>
                        </v-row>

                    </v-col>
                </v-container>
            </template>
            <v-card>
                <v-card-title>
                    Форма добавления для категории
                </v-card-title>
                <v-form>
                    <v-text-field
                        v-model="categories_name"
                        label="Название категории"
                        class="mx-5 mb-5"
                        variant="underlined"
                    >
                    </v-text-field>
                </v-form>
                <v-card-actions>
                    <v-btn color="red-accent-4"  @click="dialog = false">Закрыть</v-btn>
                    <v-btn color="green-accent-4"  @click="send_categories">Добавить</v-btn>
                </v-card-actions>
            </v-card>
        </v-dialog>  
    </div>
</template>


<script>
import axios from "axios"

export default{
    data: () => ({
        dialog: false,
        categories_name: "",
        categories: []
    }),

    mounted(){
        this.get_categories()
    },
    updated(){
        this.get_categories()
    },
    methods: {

        send_categories(){
            axios.post("http://127.0.0.1:5000/admin_panel/api/v1.0/categories", {
                id_p: 1,
                categories_name: this.categories_name
            })

            this.categories_name = "",
            this.dialog = false
        },
        get_categories(){
            axios.get("http://127.0.0.1:5000/admin_panel/api/v1.0/categories")
            .then(response  => this.categories = response.data)
        },
        delete_category(id_cat){
            axios.delete(`http://127.0.0.1:5000/admin_panel/api/v1.0/categories/${id_cat}`).then(
                (categories) => this.get_categories()
            )
        }
    }
}
</script>