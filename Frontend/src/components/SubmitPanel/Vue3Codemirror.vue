<template>
    <div class="lbder">
    <div ref="codemirrorEditor" class="codemirror-editor"></div>
    </div>
    <textarea id="saver"></textarea>
</template>

<script>
import { ref, onMounted } from 'vue';
import { EditorState } from '@codemirror/state';
import { EditorView } from '@codemirror/view';
// import { javascript } from '@codemirror/lang-javascript';
import { cpp } from '@codemirror/lang-cpp';
// import { html } from '@codemirror/lang-html';
import { oneDark } from '@codemirror/theme-one-dark';



export default {
    name: 'Vue3Codemirror',
    setup() {
        const codemirrorEditor = ref(null);

        onMounted(() => {
            const state = EditorState.create({
                doc: '',
                extensions: [
                    // javascript(),
                    cpp(),
                    // html(),
                    oneDark,
                    EditorView.updateListener.of(update => {
                        if (update.docChanged) {
                            // 获取更新后的文档内容
                            const content = update.state.doc.toString();
                            var saver=document.getElementById("saver")
                            if(saver!=null){
                                saver.value=content;
                                console.log(saver.value);
                            }
                        }
                    }),
                ],
            });

            new EditorView({
                state,
                parent: codemirrorEditor.value,
            });
        });

        return { codemirrorEditor };
    },
};
</script>

<style>
.codemirror-editor {
    height: 500px;
    width: 100%;
    border: 1px solid #ccc;
}
#saver{
    display: none;
}
.lbder{
    height: 400px;
    width: 100%;
    background-color: rgb(40, 44, 52);
    overflow: auto;
}
</style>