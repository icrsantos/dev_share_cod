package application.dao.entidades;

import javax.persistence.*;
import java.util.Date;

@Entity
@Table(name = "Usuario")
public class Usuario extends EntidadeBase{

    @Column(name = "Nome", nullable = false)
    private String nome;

    @Column(name = "Email", nullable = false)
    private String email;

    @Column(name = "Senha", nullable = false)
    private String senha;

    public Usuario(){
        this.setDataAlteracao(new Date());
    }

    public Usuario(Integer id){
        super(id);
    }

    public String getNome() { return nome; }
    public void setNome(String nome) { this.nome = nome; }

    public String getEmail() { return email; }
    public void setEmail(String email) { this.email = email; }

    public String getSenha() { return senha; }
    public void setSenha(String senha) { this.senha = senha; }

    @Override
    public String toString() {
        return "{" +
                "   \"Id\": " + this.getId() +
                "   \"DataAlteracao\": \"" + this.getDataAlteracao() + "\"" +
                "   \"Nome\": \"" + this.getNome() + "\"" +
                "   \"Senha\": \"" + this.getSenha() + "\"" +
                "}";
    }
}