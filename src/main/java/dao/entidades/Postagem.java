package dao.entidades;

import org.hibernate.annotations.Fetch;
import org.hibernate.annotations.FetchMode;
import utils.enums.EnumTipoPostagem;

import javax.persistence.*;

@Entity
@Table(name = "Postagem")
public class Postagem extends EntidadeBase{

    private static final String[] listaColunas = {
    };

    public String getEntityName() {
        return "Postagem";
    }

    public String[] getListaColunas() {
        return listaColunas;
    }

    @ManyToOne(optional = false)
    @Fetch(FetchMode.JOIN)
    @JoinColumn(name = "UsuarioId", nullable = false)
    private Usuario usuario;

    @Enumerated(EnumType.STRING)
    @Column(name = "TipoPostagem", length = 20, nullable = false)
    private EnumTipoPostagem tipoPostagem;

    @Enumerated(EnumType.STRING)
    @Column(name = "Titulo", length = 255, nullable = false)
    private String titulo;

    @Column(name = "Conteudo", length = Integer.MAX_VALUE)
    private String conteudo;

    @ManyToOne(optional = false)
    @Fetch(FetchMode.JOIN)
    @JoinColumn(name = "PostagemRespondidaId", nullable = true)
    private Postagem postagemRespondida;

    public Postagem() {
    }


    public Postagem(Integer id) {
        super(id);
    }

    @Override
    public int hashCode() {
        return toString().hashCode();
    }

    @Override
    public String toString() {
        return "{" +
                "   \"Id\": " + this.getId() +
                "   \"DataAlteracao\": \"" + this.getDataAlteracao() + "\"" +
                "   \"UsuarioId\": " + this.usuario.getId() +
                "   \"TipoPostagem\": \"" + this.getTipoPostagem() + "\"" +
                "   \"Conteudo\": \"" + this.getConteudo() + "\"" +
                "   \"PostagemRespondidaId\": " + this.postagemRespondida.getId() +
                "}";
    }

    public EnumTipoPostagem getTipoPostagem() { return tipoPostagem; }
    public void setTipoPostagem(EnumTipoPostagem tipoPostagem) { this.tipoPostagem = tipoPostagem; }

    public String getConteudo() { return conteudo; }
    public void setConteudo(String conteudo) {this.conteudo = conteudo; }

    public Postagem getPostagemRespondida() { return postagemRespondida;}
    public void setPostagemRespondida(Postagem postagemRespondida) { this.postagemRespondida = postagemRespondida; }

    public String getTitulo() { return titulo; }
    public void setTitulo(String titulo) { this.titulo = titulo; }

    public Usuario getUsuario() { return usuario;}
    public void setUsuario(Usuario usuario) { this.usuario = usuario; }
}
