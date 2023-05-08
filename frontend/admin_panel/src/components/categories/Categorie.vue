<template>
    <div class="text-center">
        <v-dialog
            v-model="dialog"
            width="auto"
        >
            <template v-slot:activator="{ props }">
                <div class="text-h3 py-6 mx-10 text-left">Молотки</div>

                <v-row class="mx-14 mt-15">
                            <v-btn  block
                                color="green-accent-4"
                                v-bind="props"
                            >
                                Добавить товар
                                </v-btn>
                </v-row>
            </template>

            <v-card>
                <v-card-title>
                Форма для добавления товара
                </v-card-title>
                <v-form>
                <v-text-field
                    v-model="brigades_name"
                    label="описание"
                    color="indigo"
                    class="mx-5"
                >

                </v-text-field>
                <v-text-field
                    v-model="brigades_name"
                    label="количество"
                    color="indigo"
                    class="mx-5"
                >

                </v-text-field>
                <v-text-field
                    v-model="brigades_name"
                    label="цвет"
                    color="indigo"
                    class="mx-5"
                >

                </v-text-field>
                <v-text-field
                    v-model="brigades_name"
                    label="цена"
                    color="indigo"
                    class="mx-5"
                >

                </v-text-field>
                </v-form>
                <v-card-actions>
                <v-btn color="red"  @click="dialog = false">Закрыть</v-btn>
                <v-btn color="green"  @click="create_brigade">Добавить</v-btn>
                </v-card-actions>
            </v-card>
        </v-dialog>
    </div>
</template>

<script>
    export default{
    data: () => ({
        dialog: false,
        quantity_characteristics: 1,
        characteristics: [],
        show_btn_delet_category: false,
        name_category: ""
    })
}
</script>